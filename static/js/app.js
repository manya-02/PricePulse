async function searchProducts() {

    const searchInput =
        document.getElementById("searchInput");

    const results =
        document.getElementById("results");

    const searchButton =
        document.querySelector(".search-container button");


    const query =
        searchInput.value.trim();


    // =============================
    // EMPTY SEARCH
    // =============================

    if (!query) {

        results.innerHTML = `
            <div class="message-card">
                <h3>Search for a product</h3>
                <p>
                    Enter a product name, model or storage variant.
                </p>
            </div>
        `;

        return;
    }


    // =============================
    // LOADING
    // =============================

    searchButton.disabled = true;

    searchButton.textContent = "Searching...";


    results.innerHTML = `
        <div class="message-card">
            <div class="loader"></div>

            <h3>Finding the best prices...</h3>

            <p>
                Comparing available offers.
            </p>
        </div>
    `;


    try {

        const response = await fetch(
            `/api/products/search?q=${encodeURIComponent(query)}`
        );


        // =============================
        // SERVER ERROR
        // =============================

        if (!response.ok) {

            throw new Error(
                `Server error: ${response.status}`
            );
        }


        const products =
            await response.json();


        // =============================
        // NO RESULTS
        // =============================

        if (
            !Array.isArray(products) ||
            products.length === 0
        ) {

            results.innerHTML = `
                <div class="message-card">

                    <h3>No products found</h3>

                    <p>
                        Try searching for another
                        product or model.
                    </p>

                </div>
            `;

            return;
        }


        // Clear loading message

        results.innerHTML = "";


        // =============================
        // DISPLAY PRODUCTS
        // =============================

        products.forEach(product => {

            const productCard =
                document.createElement("div");


            productCard.className =
                "product-card";


            const storage =
                product.storage || "N/A";


            const color =
                product.color || "N/A";


            const model =
                product.model_number ||
                product.name;


            // =============================
            // BEST PRICE
            // =============================

            let bestPriceHTML = "";


            if (product.best_price !== null) {

                bestPriceHTML = `

                    <div class="best-price">

                        <div>

                            <div class="best-price-label">
                                Best Price
                            </div>

                            <div class="best-price-value">

                                ₹${product.best_price
                                    .toLocaleString("en-IN")}

                            </div>

                            <div class="best-platform">

                                ${product.best_platform}

                            </div>

                            <div class="savings">

                                Save ₹${product.total_savings
                                    .toLocaleString("en-IN")}

                            </div>

                        </div>


                        <div>

                            ${product.offer_count}
                            platforms compared

                        </div>

                    </div>

                `;

            } else {

                bestPriceHTML = `

                    <div class="no-offers">

                        No offers currently available.

                    </div>

                `;
            }


            // =============================
            // PLATFORM OFFERS
            // =============================

            let offersHTML = "";


            if (
                product.offers &&
                product.offers.length > 0
            ) {

                product.offers.forEach(offer => {

                    const lowestBadge =
                        offer.is_lowest
                            ? `
                                <span class="lowest-badge">
                                    Lowest Price
                                </span>
                              `
                            : "";


                    offersHTML += `

                        <div class="offer ${
                            offer.is_lowest
                                ? "best-offer"
                                : ""
                        }">

                            <div class="platform-name">

                                ${offer.platform}

                                ${lowestBadge}

                            </div>


                            <div class="platform-price">

                                ₹${offer.price
                                    .toLocaleString("en-IN")}

                            </div>


                            <a
                                href="${offer.product_url}"
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                View
                            </a>

                        </div>

                    `;

                });

            } else {

                offersHTML = `

                    <div class="no-offers">

                        No platform offers found.

                    </div>

                `;
            }


            // =============================
            // PRODUCT CARD
            // =============================

            productCard.innerHTML = `

                <div class="product-header">

                    <h2>
                        ${product.name}
                    </h2>


                    <div class="product-details">

                        ${model}
                        • ${storage}
                        • ${color}

                    </div>

                </div>


                ${bestPriceHTML}


                <h3 class="offers-title">

                    Price Comparison

                </h3>


                <div class="offers">

                    ${offersHTML}

                </div>


                <div class="product-actions">

                    <button
                        class="compare-button"
                        onclick="openProduct(${product.id})"
                    >
                        Compare Prices
                    </button>

                </div>


                <div class="match-score">

                    Match Score:
                    ${product.match_score}%

                </div>

            `;


            results.appendChild(
                productCard
            );

        });


    } catch (error) {

        console.error(
            "Search error:",
            error
        );


        // =============================
        // ERROR MESSAGE
        // =============================

        results.innerHTML = `

            <div class="message-card error-card">

                <h3>
                    Something went wrong
                </h3>

                <p>
                    We couldn't complete your search.
                </p>

                <button
                    onclick="searchProducts()"
                >
                    Try Again
                </button>

            </div>

        `;

    } finally {

        // =============================
        // RESTORE BUTTON
        // =============================

        searchButton.disabled = false;

        searchButton.textContent = "Search";

    }

}


/* ============================= */
/* ENTER KEY */
/* ============================= */

function handleEnter(event) {

    if (event.key === "Enter") {

        searchProducts();

    }

}

function openProduct(productId) {

    window.location.href =
        `/product/${productId}`;

}