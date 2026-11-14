
import streamlit as st

# ==================== PAGE CONFIG ====================

st.set_page_config(
    page_title="Pizza Hub",
    page_icon="🍕",
    layout="wide"
)

# ==================== CUSTOM DESIGN ====================

st.markdown("""
<style>

/* Main website background */
.stApp {
    background-color: #FFD84D;
}

[data-testid="stHeader"] {
    background-color: #FFD84D;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* Header */
.hero-title {
    text-align: center;
    color: #C62828;
    font-size: 48px;
    font-weight: 900;
    margin-bottom: 5px;
}

.hero-subtitle {
    text-align: center;
    color: #573B16;
    font-size: 19px;
    margin-bottom: 35px;
}

/* Product cards */
[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFF9E9;
    border: 2px solid #F0B82D;
    border-radius: 18px;
    padding: 12px;
}

/* Product images */
[data-testid="stImage"] img {
    border-radius: 12px;
    height: 190px;
    object-fit: cover;
}

/* Product headings */
.menu-title {
    font-size: clamp(13px, 1.35vw, 19px);
    font-weight: 800;
    color: #A82020;
    white-space: nowrap;
    text-align: center;
    margin-top: 12px;
    margin-bottom: 20px;
}

/* General text */
.stApp, .stApp p, .stApp label {
    color: #302414;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
    justify-content: center;
}

.stTabs [data-baseweb="tab"] {
    background-color: #FFF4D1;
    border-radius: 10px;
    padding: 12px 30px;
    color: #8B2525;
    font-weight: 700;
}

.stTabs [aria-selected="true"] {
    background-color: #C62828 !important;
    color: white !important;
}

/* Buttons */
.stButton > button {
    background-color: #C62828;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    width: 100%;
    transition: 0.2s;
}

.stButton > button:hover {
    background-color: #941B1B;
    color: white;
    border: none;
}

/* Input widgets */
[data-testid="stNumberInput"] button {
    background-color: #FFE7A0;
    color: #8B2525;
}

/* Segmented control - FIXED TEXT VISIBILITY */
[data-testid="stSegmentedControl"] {
    background-color: #FFE9A8 !important;
    border-radius: 10px;
    padding: 4px;
}

/* All size options - unselected */
[data-testid="stSegmentedControl"] button {
    color: #302414 !important;
    background-color: transparent !important;
    font-weight: 700 !important;
    border-radius: 8px !important;
}

/* Selected size */
[data-testid="stSegmentedControl"] button[aria-pressed="true"] {
    background-color: #C62828 !important;
    color: #FFFFFF !important;
}

/* Hover on unselected sizes */
[data-testid="stSegmentedControl"] button:hover {
    color: #C62828 !important;
    background-color: #FFD98A !important;
}

/* Keep selected size red even when hovered */
[data-testid="stSegmentedControl"] button[aria-pressed="true"]:hover {
    background-color: #941B1B !important;
    color: #FFFFFF !important;
}

/* Price */
.price {
    font-size: 17px;
    font-weight: 700;
    text-align: center;
    margin: 12px 0;
}

.price span {
    color: #C62828;
}

.price small {
    color: #267A37;
}

/* Footer */
.footer {
    text-align: center;
    color: #694A20;
    font-size: 14px;
    margin-top: 35px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# ==================== HEADER ====================

st.markdown(
    '<div class="hero-title">🍕 Welcome to Pizza Hub</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'The best Italian restaurant serving delicious food'
    '</div>',
    unsafe_allow_html=True
)


# ==================== REUSABLE PRODUCT FUNCTION ====================

def render_product(
    name,
    image,
    key,
    fixed_price=None,
    size_prices=None
):

    with st.container(border=True):

        st.image(image, width=220)

        st.markdown(
            f'<p class="menu-title">{name}</p>',
            unsafe_allow_html=True
        )

        if size_prices is not None:

            size = st.segmented_control(
                "Size:",
                options=list(size_prices.keys()),
                default="Medium",
                key=f"{key}_size"
            )

            price = size_prices[size]

        else:
            price = fixed_price

        st.markdown(
            f'<div class="price">'
            f'Price: <span>{price}</span> '
            f'<small>EGP</small>'
            f'</div>',
            unsafe_allow_html=True
        )

        quantity = st.number_input(
            "Quantity:",
            min_value=1,
            max_value=10,
            value=1,
            step=1,
            key=f"{key}_quantity"
        )

        total = price * quantity

        if st.button(
            "Calculate Total Price",
            key=f"{key}_calculate"
        ):

            st.success(
                f"{name} × {quantity} = {total} EGP"
            )


# ==================== MENU TABS ====================

pizza_tab, pasta_tab, drinks_tab = st.tabs([
    "🍕 Pizza",
    "🍝 Pasta",
    "🥤 Drinks"
])


# ==================== PIZZA TAB ====================

with pizza_tab:

    col1, col2, col3 = st.columns(3)

    with col1:
        render_product(
            name="Chicken Pizza",
            image="https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=1000&q=80",
            key="chicken_pizza",
            size_prices={
                "Small": 120,
                "Medium": 200,
                "Large": 300
            }
        )

    with col2:
        render_product(
            name="Pepperoni Pizza",
            image="https://pizzano.co.in/assets/images/gallery/pepperoni_pizza_product_shot.png",
            key="pepperoni_pizza",
            size_prices={
                "Small": 150,
                "Medium": 250,
                "Large": 350
            }
        )

    with col3:
        render_product(
            name="Margherita Pizza",
            image="https://cdn.shopify.com/s/files/1/0851/3955/4638/files/Classic_Cheese_Pizza_with_Golden_Crust_and_Melted_Mozzarella.webp?v=1747591495",
            key="margherita_pizza",
            size_prices={
                "Small": 100,
                "Medium": 180,
                "Large": 250
            }
        )


# ==================== PASTA TAB ====================

with pasta_tab:

    col1, col2, col3 = st.columns(3)

    with col1:
        render_product(
            name="Red Sauce Pasta",
            image="https://miro.medium.com/v2/resize:fit:736/1*HqJFqDEhRGLp73jxpkMpiA@2x.jpeg",
            key="red_sauce",
            size_prices={
                "Small": 80,
                "Medium": 120,
                "Large": 150
            }
        )

    with col2:
        render_product(
            name="Chicken Alfredo Pasta",
            image="https://myhomemaderecipe.com/assets/images/Ultimate-Comfort-Food-with-Chicken-Alfredo-hero.jpg",
            key="chicken_alfredo",
            size_prices={
                "Small": 100,
                "Medium": 140,
                "Large": 180
            }
        )

    with col3:
        render_product(
            name="Pesto Pasta",
            image="https://images.unsplash.com/photo-1473093295043-cdd812d0e601?auto=format&fit=crop&w=1000&q=80",
            key="pesto",
            size_prices={
                "Small": 90,
                "Medium": 130,
                "Large": 170
            }
        )


# ==================== DRINKS TAB ====================

with drinks_tab:

    col1, col2, col3 = st.columns(3)

    with col1:
        render_product(
            name="Orange Juice",
            image="https://static.wixstatic.com/media/cf8a7a_8b57d45e0bf34139b2f9486f56037623~mv2.jpg/v1/fill/w_2500%2Ch_2500%2Cal_c/cf8a7a_8b57d45e0bf34139b2f9486f56037623~mv2.jpg",
            key="orange_juice",
            fixed_price=30
        )

    with col2:
        render_product(
            name="Fresh Lemonade",
            image="https://static.wixstatic.com/media/94064a_663b580963db4712862241d304ff3833~mv2.png/v1/fill/w_480%2Ch_480%2Cal_c%2Cq_85%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/94064a_663b580963db4712862241d304ff3833~mv2.png",
            key="fresh_lemonade",
            fixed_price=35
        )

    with col3:
        render_product(
            name="Iced Cola",
            image="https://images.unsplash.com/photo-1554866585-cd94860890b7?auto=format&fit=crop&w=1000&q=80",
            key="iced_cola",
            fixed_price=25
        )


# ==================== FOOTER ====================

st.markdown("""
<div class="footer">
    🍕 Pizza Hub | Fresh Food, Delicious Moments
</div>
""", unsafe_allow_html=True)
