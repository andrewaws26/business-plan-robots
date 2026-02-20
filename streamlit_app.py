import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="The Blueprint", 
    page_icon="📖", 
    layout="centered" # Changed to centered for a better reading experience
)

# 2. Custom CSS for a "Scrollytelling" Editorial Feel
st.markdown("""
<style>
    /* Hero Section */
    .hero-title {
        font-size: 56px;
        font-weight: 900;
        color: #0F172A;
        text-align: center;
        margin-top: 50px;
        margin-bottom: 10px;
        line-height: 1.1;
    }
    .hero-subtitle {
        font-size: 24px;
        color: #64748B;
        text-align: center;
        margin-bottom: 80px;
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
        margin-bottom: 20px;
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
        border-radius: 8px;
        border-left: 4px solid #0F172A;
        margin: 40px 0;
        font-size: 18px;
        color: #475569;
        font-style: italic;
    }
    
    /* Divider */
    .story-divider {
        height: 1px;
        background-color: #E2E8F0;
        margin: 60px 0;
    }
</style>
""", unsafe_allow_html=True)

# 3. The Hero Section
st.markdown('<div class="hero-title">The Kentucky Crucible</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">A 24-month roadmap from the rail yard to financial independence.</div>', unsafe_allow_html=True)

# 4. Chapter 1
st.markdown('<div class="chapter-number">Chapter 01</div>', unsafe_allow_html=True)
st.markdown('<div class="chapter-title">The Foundation of Dirt and Code</div>', unsafe_allow_html=True)
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

# 5. Chapter 2
st.markdown('<div class="chapter-number">Chapter 02</div>', unsafe_allow_html=True)
st.markdown('<div class="chapter-title">The Unfair Advantage</div>', unsafe_allow_html=True)
st.markdown("""
<div class="story-text">
Traditional engineers are siloed. They either understand the mechanical load paths, or they understand the high-level C# architecture, or they understand the business ROI. Rarely do they understand all three.
<br><br>
But there is a fourth multiplier: Shenzhen. Six months on the ground in the manufacturing capital of the world, combined with absolute fluency in Mandarin, shatters the traditional supply chain. This isn't just an engineering profile anymore; it is an international arbitrage machine.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="story-divider"></div>', unsafe_allow_html=True)

# 6. Chapter 3
st.markdown('<div class="chapter-number">Chapter 03</div>', unsafe_allow_html=True)
st.markdown('<div class="chapter-title">The Divergence</div>', unsafe_allow_html=True)
st.markdown("""
<div class="story-text">
At the end of year two, the path splits into two distinct, highly lucrative directions. The choice depends entirely on the desired lifestyle.
</div>
""", unsafe_allow_html=True)

# Split into two columns for the final decision
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### Path A: The Equity Leap")
    st.markdown("""
    <div style="font-size: 18px; color: #475569; line-height: 1.6;">
    The aerospace route. Companies like SpaceX desperately need builders who can navigate the ambiguity of bringing up prototype hardware. The massive value here lies in restricted stock units (RSUs) and private tender offers. You trade 60-hour weeks for a highly accelerated, multi-million dollar liquidity event.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### Path B: The Integrator Empire")
    st.markdown("""
    <div style="font-size: 18px; color: #475569; line-height: 1.6;">
    The B2B route. Leveraging the business degree and Mandarin fluency to bypass US middlemen. Sourcing bare-metal cobots directly from Guangdong on Net-60 terms, wrapping them in custom software logic, and selling $85,000 turnkey solutions to Midwest factories using a cash-flow positive 50/40/10 model. Complete autonomy.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="story-divider"></div>', unsafe_allow_html=True)

# 7. Footer
st.markdown("""
<div style="text-align: center; color: #94A3B8; font-size: 16px; margin-bottom: 50px;">
The code is written. The hardware is waiting.
</div>
""", unsafe_allow_html=True)
