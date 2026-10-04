document.addEventListener("DOMContentLoaded", () => {

    loadProduct();

});


async function loadProduct() {

    const container = document.getElementById("productDetails");

    const pathParts = window.location.pathname.split("/");

    const productId = pathParts[pathParts.length - 1];


    if (!productId || isNaN(productId)) {

        showError(
            "Invalid product",
            "The product you are looking for could not be found."
        );

        return;

    }


    try {

        const response = await fetch(
            `/api/products/${productId}`
        );


        if (!response.ok) {

            throw new Error("Product not found");

        }


        const data = await response.json();


        if (!data || !data.product) {

            throw new Error("Product not found");

        }


        displayProduct(data);

    }

    catch (error) {

        console.error(error);

        showError(
            "Product not found",
            "We could not find this product."
        );

    }

}


function displayProduct(data) {

    const container = document.getElementById("productDetails");

    const product = data.product;

    const offers = data.offers || [];


    const lowestPrice = data.lowest_price;

    const highestPrice = data.highest_price;

    const savings = data.savings;

    const savingPercentage = data.saving_percentage;


    let offersHTML = "";


    if (offers.length === 0) {

        offersHTML = `
            <div class="message-card">

                <h3>
                    No offers available
                </h3>

                <p>
                    There are currently no available offers
                    for this product.
                </p>

            </div>
        `;

    }

    else {

        offersHTML = offers.map((offer, index) => {

            const price = formatPrice(offer.price);

            const originalPrice =
                offer.original_price
                    ? formatPrice(offer.original_price)
                    : "";

            const isLowest =
                index === 0 ||
                offer.price === lowestPrice;


            return `

                <div class="platform-card
                    ${isLowest ? "best-deal" : ""}">

                    <div class="platform-card-top">

                        <div>

                            <div class="platform-name">

                                ${escapeHTML(
                                    offer.platform || "Platform"
                                )}

                            </div>

                            ${
                                isLowest
                                ? `
                                    <span class="best-price-badge">
                                        LOWEST PRICE
                                    </span>
                                  `
                                : ""
                            }

                        </div>


                        <div class="availability">

                            ${
                                offer.availability
                                    ? escapeHTML(
                                        offer.availability
                                      )
                                    : "Available"
                            }

                        </div>

                    </div>


                    <div class="platform-price">

                        <span class="current-price">
                            ₹${price}
                        </span>

                        ${
                            originalPrice
                                ? `
                                    <span class="original-price">
                                        ₹${originalPrice}
                                    </span>
                                  `
                                : ""
                        }

                    </div>


                    ${
                        offer.original_price &&
                        offer.original_price > offer.price
                            ? `
                                <div class="offer-saving">

                                    Save ₹${formatPrice(
                                        offer.original_price -
                                        offer.price
                                    )}

                                </div>
                              `
                            : ""
                    }


                    <a
                        href="${offer.product_url || "#"}"
                        target="_blank"
                        rel="noopener noreferrer"
                        class="buy-button"
                        ${
                            !offer.product_url
                                ? 'onclick="return false;"'
                                : ""
                        }
                    >

                        View Deal →

                    </a>

                </div>

            `;

        }).join("");

    }


    container.innerHTML = `

        <section class="product-page">


            <!-- PRODUCT INFORMATION -->

            <div class="product-overview">


                <div class="product-image-area">

                    ${
                        product.image_url
                            ? `
                                <img
                                    src="${escapeHTML(
                                        product.image_url
                                    )}"
                                    alt="${escapeHTML(
                                        product.name
                                    )}"
                                    class="product-image"
                                >
                              `
                            : `
                                <div class="product-image-placeholder">

                                    <span>PRODUCT</span>

                                </div>
                              `
                    }

                </div>


                <div class="product-information">

                    <span class="section-label">
                        PRODUCT DETAILS
                    </span>


                    <h1>
                        ${escapeHTML(product.name)}
                    </h1>


                    ${
                        product.brand
                            ? `
                                <p class="product-brand">
                                    ${escapeHTML(product.brand)}
                                </p>
                              `
                            : ""
                    }


                    <div class="product-meta">

                        ${
                            product.storage
                                ? `
                                    <span>
                                        ${escapeHTML(
                                            product.storage
                                        )}
                                    </span>
                                  `
                                : ""
                        }

                        ${
                            product.color
                                ? `
                                    <span>
                                        ${escapeHTML(
                                            product.color
                                        )}
                                    </span>
                                  `
                                : ""
                        }

                        ${
                            product.category
                                ? `
                                    <span>
                                        ${escapeHTML(
                                            product.category
                                        )}
                                    </span>
                                  `
                                : ""
                        }

                    </div>


                    ${
                        product.description
                            ? `
                                <p class="product-description">
                                    ${escapeHTML(
                                        product.description
                                    )}
                                </p>
                              `
                            : ""
                    }


                    <div class="product-summary">

                        <div class="summary-item">

                            <span>
                                Lowest price
                            </span>

                            <strong>
                                ${
                                    lowestPrice !== null &&
                                    lowestPrice !== undefined
                                        ? `₹${formatPrice(
                                            lowestPrice
                                          )}`
                                        : "—"
                                }
                            </strong>

                        </div>


                        <div class="summary-item">

                            <span>
                                Highest price
                            </span>

                            <strong>
                                ${
                                    highestPrice !== null &&
                                    highestPrice !== undefined
                                        ? `₹${formatPrice(
                                            highestPrice
                                          )}`
                                        : "—"
                                }
                            </strong>

                        </div>


                        <div class="summary-item">

                            <span>
                                Maximum savings
                            </span>

                            <strong>
                                ${
                                    savings !== null &&
                                    savings !== undefined
                                        ? `₹${formatPrice(
                                            savings
                                          )}`
                                        : "—"
                                }
                            </strong>

                        </div>


                        <div class="summary-item">

                            <span>
                                Savings
                            </span>

                            <strong>
                                ${
                                    savingPercentage !== null &&
                                    savingPercentage !== undefined
                                        ? `${Number(
                                            savingPercentage
                                          ).toFixed(1)}%`
                                        : "—"
                                }
                            </strong>

                        </div>

                    </div>

                </div>

            </div>


            <!-- PLATFORM COMPARISON -->

            <section class="comparison-section">

                <div class="section-heading">

                    <span class="section-label">
                        PRICE COMPARISON
                    </span>

                    <h2>
                        Compare available offers
                    </h2>

                    <p>
                        Check the available prices across
                        different shopping platforms.
                    </p>

                </div>


                <div class="platform-grid">

                    ${offersHTML}

                </div>

            </section>


            <!-- BACK BUTTON -->

            <div class="product-actions">

                <a
                    href="/"
                    class="back-button"
                >
                    ← Search another product
                </a>

            </div>


        </section>

    `;

}


function showError(title, message) {

    const container =
        document.getElementById("productDetails");


    container.innerHTML = `

        <div class="message-card error-card">

            <div class="error-icon">
                !
            </div>

            <h2>
                ${escapeHTML(title)}
            </h2>

            <p>
                ${escapeHTML(message)}
            </p>

            <a
                href="/"
                class="back-button"
            >
                ← Back to search
            </a>

        </div>

    `;

}


function formatPrice(value) {

    const number = Number(value);


    if (isNaN(number)) {

        return "0";

    }


    return number.toLocaleString("en-IN");

}


function escapeHTML(value) {

    if (value === null || value === undefined) {

        return "";

    }


    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");

}