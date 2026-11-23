import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ayesha Khalid | Content Strategist & Creative Writer",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR ORGANIC WARM PALETTE (CREAM, PEACH, TERRACOTTA RED) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,700;1,9..40,400&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap');

    /* Main Background - Warm Cream */
    .stApp {
        background-color: #FDF6EE;
        color: #3D1E16;
        font-family: 'DM Sans', sans-serif;
    }

    /* Hide default Streamlit header/footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Typography */
    h1, h2, h3, .serif-title {
        font-family: 'Playfair Display', serif !important;
        color: #A83820 !important;
    }

    /* Hero Arch Graphic (Recreated from PDF) */
    .hero-arch {
        width: 100%;
        max-width: 340px;
        height: 400px;
        margin: 0 auto;
        background: linear-gradient(180deg, #D5EEFA 0%, #EAF6FC 75%);
        border-radius: 170px 170px 16px 16px;
        border: 14px solid #B53D22;
        position: relative;
        overflow: hidden;
        box-shadow: 0 12px 30px rgba(181, 61, 34, 0.15);
    }

    .cloud {
        width: 140px;
        height: 45px;
        background: #FFFFFF;
        border-radius: 50px;
        position: absolute;
        top: 65px;
        left: 50%;
        transform: translateX(-50%);
    }
    .cloud::before {
        content: '';
        width: 70px;
        height: 70px;
        background: #FFFFFF;
        border-radius: 50%;
        position: absolute;
        top: -32px;
        left: 35px;
    }

    .hill-back {
        width: 140%;
        height: 110px;
        background: #B9D882;
        border-radius: 50%;
        position: absolute;
        bottom: -35px;
        left: -30%;
    }
    .hill-front {
        width: 140%;
        height: 105px;
        background: #779A18;
        border-radius: 50%;
        position: absolute;
        bottom: -45px;
        right: -25%;
    }

    /* Section Containers */
    .peach-banner {
        background-color: #FBE6D4;
        border-radius: 24px;
        padding: 3rem 2.5rem;
        margin: 2rem 0;
        border: 1px solid #F3D0B5;
    }

    .terracotta-banner {
        background-color: #B53D22;
        color: #FDF6EE !important;
        border-radius: 24px;
        padding: 3rem 2.5rem;
        margin: 2rem 0;
    }
    .terracotta-banner h2, .terracotta-banner h3, .terracotta-banner p {
        color: #FDF6EE !important;
    }

    /* Service Cards */
    .service-card {
        background-color: #FFFBF7;
        border: 1.5px solid #F2C9AE;
        border-radius: 16px;
        padding: 1.4rem 1.2rem;
        text-align: center;
        height: 100%;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 4px 12px rgba(181, 61, 34, 0.05);
    }
    .service-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(181, 61, 34, 0.12);
        border-color: #B53D22;
    }
    .service-title {
        font-weight: 700;
        font-size: 1.05rem;
        color: #8C2B15;
        margin-top: 0.4rem;
    }

    /* Client Pill Cards */
    .client-card {
        background-color: #FBE6D4;
        border-radius: 50px;
        padding: 1.1rem 1.5rem;
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 1.2rem;
        font-weight: 600;
        color: #8C2B15;
        border: 1px solid #EBBFA0;
    }

    /* Custom Buttons */
    .stButton > button {
        background-color: #B53D22 !important;
        color: #FDF6EE !important;
        border-radius: 50px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        border: none !important;
        transition: background-color 0.2s ease !important;
    }
    .stButton > button:hover {
        background-color: #8E2C16 !important;
    }

    /* Anchor Link Buttons */
    .cta-link {
        display: inline-block;
        background-color: #B53D22;
        color: #FDF6EE !important;
        text-decoration: none;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        margin-top: 1rem;
        transition: background-color 0.2s ease;
    }
    .cta-link:hover {
        background-color: #8E2C16;
    }
    .cta-link-light {
        display: inline-block;
        background-color: #FBE6D4;
        color: #8E2C16 !important;
        text-decoration: none;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        font-weight: 700;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)


# --- HERO SECTION ---
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("""
        <div class="hero-arch">
            <div class="cloud"></div>
            <div class="hill-back"></div>
            <div class="hill-front"></div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<div style='padding-top: 2rem;'></div>", unsafe_allow_html=True)
    st.markdown(
        "<h1 style='font-size: 3.3rem; line-height: 1.15; margin-bottom: 1rem;'>"
        "Looking for a content strategist and a creative writer?</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='font-size: 1.3rem; color: #5C3226; margin-bottom: 1.5rem;'>"
        "See how your business benefits.</p>",
        unsafe_allow_html=True
    )
    st.markdown('<a href="#about-me" class="cta-link">Learn More ↓</a>', unsafe_allow_html=True)


# --- ABOUT ME SECTION ---
st.markdown('<div id="about-me"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="peach-banner">
    <h2 style="font-size: 2.3rem; margin-bottom: 1rem;">About Me</h2>
    <p style="font-size: 1.2rem; line-height: 1.75; color: #3D1E16; max-width: 850px;">
        I'm <strong>Ayesha Khalid</strong>, a writer who lives where search algorithms meet storytelling. 
        I've spent my career helping brands get found and remembered. I specialise in 
        <strong>SEO, AEO, and GEO content</strong>, and as a published writer in anthologies and newsletters, 
        I bring a storyteller's eye to every strategy.
    </p>
    <a href="#contact-me" class="cta-link">Work with Me</a>
</div>
""", unsafe_allow_html=True)


# --- SERVICES SECTION ---
st.markdown("<h2 style='text-align: center; font-size: 2.4rem; margin: 2.5rem 0 1.5rem 0;'>Ways I Help Brands Grow</h2>", unsafe_allow_html=True)

services = [
    ("🧭", "Content Strategy"),
    ("🖋️", "Ghostwriting"),
    ("📱", "Social Media Content and Strategy"),
    ("🔍", "Search-Driven Long-Form Content Writing"),
    ("🎨", "Canva Designing"),
    ("🎬", "Script Writing"),
    ("✂️", "Editing"),
    ("✅", "Proofreading"),
]

# Render 4x2 grid
for row_idx in range(0, len(services), 4):
    cols = st.columns(4, gap="medium")
    for col_idx, (icon, title) in enumerate(services[row_idx:row_idx+4]):
        with cols[col_idx]:
            st.markdown(f"""
                <div class="service-card">
                    <div style="font-size: 1.8rem;">{icon}</div>
                    <div class="service-title">{title}</div>
                </div>
            """, unsafe_allow_html=True)
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)


# --- CLIENTS SECTION ---
st.markdown("<h2 style='text-align: center; font-size: 2.4rem; margin: 2.5rem 0 1.5rem 0;'>Clients</h2>", unsafe_allow_html=True)

clients = [
    "Fleure Beauty",
    "Great Nature Spa & Salon",
    "Tressande"
]

c_cols = st.columns(3, gap="medium")
for idx, client in enumerate(clients):
    with c_cols[idx]:
        st.markdown(f'<div class="client-card">{client}</div>', unsafe_allow_html=True)


# --- CONTACT & FREE PROPOSAL SECTION ---
st.markdown('<div id="contact-me"></div>', unsafe_allow_html=True)
st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

contact_col1, contact_col2 = st.columns([1, 1.2], gap="large")

with contact_col1:
    st.markdown("""
    <div class="terracotta-banner" style="height: 100%; margin: 0;">
        <h2 style="font-size: 2.3rem; margin-bottom: 0.5rem;">Contact Me</h2>
        <p style="font-size: 1.15rem; opacity: 0.9; margin-bottom: 2rem;">
            Ready to blend search visibility with memorable brand storytelling? Let's talk.
        </p>
        <p style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.8rem;">Ayesha Khalid</p>
        <p style="font-size: 1.1rem; margin-bottom: 0.6rem;">📞 <a href="tel:+919288668821" style="color: #FDF6EE; text-decoration: none;">+91 9288668821</a></p>
        <p style="font-size: 1.1rem; margin-bottom: 1.5rem;">✉️ <a href="mailto:ayeshakhalid.cw@gmail.com" style="color: #FDF6EE; text-decoration: none;">ayeshakhalid.cw@gmail.com</a></p>
    </div>
    """, unsafe_allow_html=True)

with contact_col2:
    st.markdown("<h3 style='font-size: 1.8rem; margin-top: 0;'>Get a Free Proposal</h3>", unsafe_allow_html=True)
    with st.form("proposal_form", clear_on_submit=True):
        name = st.text_input("Your Name / Brand Name *")
        email = st.text_input("Your Email Address *")
        selected_services = st.multiselect(
            "Which services are you interested in?",
            [s[1] for s in services],
            default=["Content Strategy"]
        )
        project_details = st.text_area("Tell me a bit about your goals, timeline, or content needs:")
        submitted = st.form_submit_button("Get a free proposal")

        if submitted:
            if not name or not email:
                st.error("Please provide both your name and email address.")
            else:
                st.success(f"Thank you, {name}! Your proposal request has been recorded. Ayesha will reach out to {email} shortly.")