import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="The Blueprint", 
    page_icon="📖", 
    layout="centered"
)

# 2. Custom CSS for Editorial Feel & Image Styling
st.markdown("""
<style>
    /* Main container spacing */
    .main .block-container {
        max-width: 800px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    /* Hero Section Typography */
    .hero-title {
        font-size: 56px;
        font-weight: 900;
        color: #0F172A;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
        line-height: 1.1;
    }
    .hero-subtitle {
        font-size: 24px;
        color: #64748B;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 300;
    }
    
    /* Chapter Formatting */
    .chapter-number {
        font-size: 16px;
        font-weight: bold;
        color: #2563EB;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: -10px;
        margin-top: 60px;
    }
    .chapter-title {
        font-size: 36px;
        font-weight: 800;
        color: #1E293B;
        margin-bottom: 30px;
    }
    .story-text {
        font-size: 20px;
        color: #334155;
        line-height: 1.8;
        margin-bottom: 30px;
    }
    
    /* Highlight Cards inside the story */
    .story-card {
        background-color: #F8FAFC;
        padding: 30px;
        border-radius: 12px;
        border-left: 4px solid #0F172A;
        margin: 40px 0;
        font-size: 19px;
        color: #475569;
        font-style: italic;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    
    /* Image Styling to make st.image look premium */
    img {
        border-radius: 12px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        margin-bottom: 30px;
    }
    
    /* Divider */
    .story-divider {
        height: 1px;
        background-color: #E2E8F0;
        margin: 80px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
# Image: Rugged industrial robotic arm in a dark factory setting
st.image("https://images.unsplash.com/photo-1565105226520-426543250113?q=80&w=1000&auto=format&fit=crop", use_container_width=True)
st.markdown('<div class="hero-title">The Kentucky Crucible</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">A visual roadmap from the rail yard to financial independence.</div>', unsafe_allow_html=True)

st.markdown('<div class="story-divider"></div>', unsafe_allow_html=True)

# --- CHAPTER 1 ---
st.markdown('<div class="chapter-number">Chapter 01</div>', unsafe_allow_html=True)
st.markdown('<div class="chapter-title">The Foundation of Dirt and Code</div>', unsafe_allow_html=True)

# Image: Heavy industry/metalwork representing the physical challenge
st.image("https://images.unsplash.com/photo-1535203111783-29927010581b?q=80&w=1000&auto=format&fit=crop", caption="Where abstract code meets heavy physics.", use_container_width=True)

st.markdown("""
<div class="story-text">
The journey doesn't start in a sterile Silicon Valley office. It starts in a heavy-duty rail yard, surrounded by 200-pound wooden ties and the noise of pneumatic grippers. 
<br><br>
This is the crucible. The goal here isn't just to write code; it's to force a collision between an object-oriented software background and the rigid, unforgiving reality of industrial physics. By implementing Finite State Machines into legacy Val3 code, bridging AI vision systems, and mastering offline 3D simulation, a unique engineer is forged. One who doesn't just theorize, but builds.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="story-card">
"In 24 months, the transformation is complete. The software engineer becomes a battle-tested robotic integrator, capable of shaving seconds off a cycle time while keeping the hardware intact."
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="story-divider"></div>', unsafe_allow_html=True)

# --- CHAPTER 2 ---
st.markdown('<div class="chapter-number">Chapter 02</div>', unsafe_allow_html=True)
st.markdown('<div class="chapter-title">The Unfair Advantage</div>', unsafe_allow_html=True)

# Image: Shipping port/containers representing global supply chain and Shenzhen
st.image("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=1000&auto=format&fit=crop", caption="Leveraging the speed of the Shenzhen supply chain.", use_container_width=True)

st.markdown("""
<div class="story-text">
Traditional engineers are siloed. They either understand the mechanical load paths, or they understand the high-level C# architecture, or they understand the business ROI. Rarely do they understand all three.
<br><br>
But there is a fourth multiplier: Shenzhen. Six months on the ground in the manufacturing capital of the world, combined with absolute fluency in Mandarin, shatters the traditional supply chain. This isn't just an engineering profile anymore; it is an international arbitrage machine.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="story-divider"></div>', unsafe_allow_html=True)

# --- CHAPTER 3 ---
st.markdown('<div class="chapter-number">Chapter 03</div>', unsafe_allow_html=True)
st.markdown('<div class="chapter-title">The Divergence</div>', unsafe_allow_html=True)
st.markdown("""
<div class="story-text">
At the end of year two, the path splits into two distinct, highly lucrative directions. The choice depends entirely on the desired lifestyle.
</div>
""", unsafe_allow_html=True)

# Split into two columns for the final decision with distinct images
col1, col2 = st.columns(2, gap="medium")

with col1:
    # Image: Aerospace/Rocketry
    st.image("https://images.unsplash.com/photo-1516849841032-87cbac4d88f7?q=80&w=1000&auto=format&fit=crop", use_container_width=True)
    st.markdown("### Path A: The Equity Leap")
    st.markdown("""
    <div style="font-size: 18px; color: #475569; line-height: 1.6;">
    **The Aerospace Route.** Companies like SpaceX desperately need builders who can navigate prototype hardware. The value lies in restricted stock units (RSUs) and private tender offers. You trade 60-hour weeks for a highly accelerated, multi-million dollar liquidity event.
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Image: A smaller, collaborative robot representing agile B2B integration
    st.image("https://images.unsplash.com/photo-1637401629606-855089e023fb?q=80&w=1000&auto=format&fit=crop", use_container_width=True)
    st.markdown("### Path B: The Integrator Empire")
    st.markdown("""
    <div style="font-size: 18px; color: #475569; line-height: 1.6;">
    **The B2B Route.** Leveraging the business degree and Mandarin fluency to bypass US middlemen. Sourcing bare-metal cobots directly from Guangdong on Net-60 terms and selling turnkey solutions using a cash-flow positive model. Complete autonomy.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="story-divider"></div>', unsafe_allow_html=True)

# 7. Footer
st.markdown("""
<div style="text-align: center; color: #94A3B8; font-size: 16px; margin-bottom: 50px;">
The code is written. The hardware is waiting.
</div>
""", unsafe_allow_html=True)
