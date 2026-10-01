async function loadProduct() {

    const container =
        document.getElementById("productDetails");


    // ==========================================
    // GET PRODUCT ID
    // ==========================================

    const parts =
        window.location.pathname.split("/");

    const productId =
        parts[parts.length - 1];


    try {

        // ==========================================
        // GET PRODUCT DATA
        // ==========================================

        const response = await fetch(
            `/api/products/${productId}`
        );


        if (!response.ok) {

            throw new Error(
                "Product not found"
            );

        }


        const product =
            await response.json();


        // ==========================================
        // PRODUCT IMAGE
        // ==========================================

        let imageHTML = "";

        if (product.image_url) {

            imageHTML = `
                <img
                    src="${product.image_url}"
                    alt="${product.name}"
                    class="product-image"
                >
            `;

        } else {

            imageHTML = `
                <div class="product-image-placeholder">
                    📦
                </div>
            `;

        }


        // ==========================================
        // CALCULATE DISCOUNT
        // ==========================================

        let discountHTML = "";


        if (
            product.highest_price &&
            product.best_price &&
            product.highest_price >
            product.best_price
        ) {

            const discount =
                Math.round(
                    (
                        (
                            product.highest_price
                            - product.best_price
                        )
                        /
                        product.highest_price
                    ) * 100
                );


            discountHTML = `

                <div class="discount">

                    ${discount}% lower than highest price

                </div>

            `;

        }


        // ==========================================
        // OFFERS
        // ==========================================

        let offersHTML = "";


        if (
            product.offers &&
            product.offers.length > 0
        ) {

            product.offers.forEach(
                offer => {

                    const lowestBadge =
                        offer.is_lowest
                            ? `
                                <span class="lowest-badge">
                                    Lowest Price
                                </span>
                              `
                            : "";


                    let originalPriceHTML = "";


                    if (
                        offer.original_price &&
                        offer.original_price >
                        offer.price
                    ) {

                        originalPriceHTML = `

                            <div class="original-price">

                                ₹${offer.original_price
                                    .toLocaleString("en-IN")}

                            </div>

                        `;

                    }


                    offersHTML += `

                        <div class="platform-card ${
                            offer.is_lowest
                                ? "lowest-platform"
                                : ""
                        }">


                            <div class="platform-info">

                                <div class="platform-name">

                                    ${offer.platform}

                                    ${lowestBadge}

                                </div>


                                <div class="availability">

                                    ${offer.availability}

                                </div>

                            </div>


                            <div class="platform-price-section">

                                ${originalPriceHTML}

                                <div class="platform-price">

                                    ₹${offer.price
                                        .toLocaleString("en-IN")}

                                </div>

                            </div>


                            <a
                                href="${offer.product_url}"
                                target="_blank"
                                rel="noopener noreferrer"
                                class="buy-button"
                            >
                                View Deal
                            </a>


                        </div>

                    `;

                }
            );

        } else {

            offersHTML = `

                <div class="no-offers">

                    No offers currently available.

                </div>

            `;

        }


        // ==========================================
        // PRODUCT PAGE
        // ==========================================

        container.innerHTML = `

            <button
                class="back-button"
                onclick="window.location.href='/'"
            >
                ← Back to Search
            </button>


            <div class="product-page">


                <!-- PRODUCT INFORMATION -->

                <div class="product-info-section">


                    <div class="product-image-section">

                        ${imageHTML}

                    </div>


                    <div class="product-main-info">

                        <div class="category-label">

                            ${product.category || "Product"}

                        </div>


                        <h1>

                            ${product.name}

                        </h1>


                        <div class="product-meta">

                            <span>
                                Brand: ${product.brand || "N/A"}
                            </span>

                            <span>
                                Storage: ${product.storage || "N/A"}
                            </span>

                            <span>
                                Color: ${product.color || "N/A"}
                            </span>

                        </div>


                        <p class="product-description">

                            ${product.description || ""}

                        </p>


                        <div class="best-price-large">


                            <div class="best-price-label">

                                Best Available Price

                            </div>


                            <div class="best-price-large-value">

                                ${
                                    product.best_price !== null
                                    ? "₹" +
                                      product.best_price
                                      .toLocaleString("en-IN")
                                    : "Not available"
                                }

                            </div>


                            <div class="best-platform">

                                ${
                                    product.best_platform
                                    || ""
                                }

                            </div>


                            ${discountHTML}

                        </div>

                    </div>

                </div>


                <!-- PRICE COMPARISON -->

                <div class="comparison-section">


                    <div class="comparison-header">

                        <div>

                            <h2>
                                Price Comparison
                            </h2>

                            <p>
                                Compare prices from
                                ${product.offer_count}
                                platforms
                            </p>

                        </div>


                        <div class="total-savings">

                            Save up to

                            <strong>
                                ₹${product.total_savings
                                    .toLocaleString("en-IN")}
                            </strong>

                        </div>

                    </div>


                    <div class="platform-list">

                        ${offersHTML}

                    </div>

                </div>


            </div>

        `;

    }


    catch (error) {

        console.error(
            "Product loading error:",
            error
        );


        container.innerHTML = `

            <div class="message-card error-card">

                <h3>
                    Product not found
                </h3>

                <p>
                    We couldn't load this product.
                </p>


                <button
                    onclick="window.location.href='/'"
                >
                    Back to Search
                </button>

            </div>

        `;

    }

}


// ==========================================
// LOAD PRODUCT
// ==========================================

loadProduct();