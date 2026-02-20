import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="The Automation Blueprint", 
    page_icon="⚙️", 
    layout="wide"
)

# 2. Custom CSS for UI Enhancement
st.markdown("""
<style>
    .main-header {
        font-size: 42px;
        font-weight: 900;
        color: #0F172A;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 22px;
        color: #64748B;
        text-align: center;
        margin-bottom: 40px;
    }
    .card {
        background-color: #F8FAFC;
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid #3B82F6;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        height: 100%;
    }
    .highlight {
        color: #2563EB;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 3. Headers
st.markdown('<div class="main-header">The Automation & Wealth Blueprint</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Transitioning from Software Engineering to Industrial Empire</div>', unsafe_allow_html=True)

# 4. Interactive Tabs
tab1, tab2, tab3 = st.tabs(["🏗️ Phase 1: The Crucible", "🚀 Phase 2A: The Equity Leap", "🌍 Phase 2B: The Integrator Empire"])

# --- TAB 1: Current State ---
with tab1:
    st.markdown("### The Crucible (Months 1-24)")
    st.info("**Primary Objective:** Transform pure software architecture skills into battle-tested mechatronic capability.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
        <h4>Core Technical Benchmarks</h4>
        <ul>
            <li><b>Procedural Optimization:</b> Implement Finite State Machines (FSM) to eliminate nested industrial code logic.</li>
            <li><b>Cycle Time Reduction:</b> Master motion blending and asynchronous I/O vision polling to push output to sprint capacity.</li>
            <li><b>Virtual Commissioning:</b> Utilize 3D simulation engines to validate hardware safety offline.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card">
        <h4>Controls & Floor Integration</h4>
        <ul>
            <li><b>PLC Architecture:</b> Map electrical cabinet wiring and ladder logic to bridge AI vision networks with servo drives.</li>
            <li><b>Safety Protocols:</b> Ensure system compliance with rigid industrial safety standards.</li>
            <li><b>Cross-Disciplinary Trust:</b> Translate high-level codebase changes into pragmatic language for floor mechanics.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: Aerospace/Big Tech ---
with tab2:
    st.markdown("### The Equity Leap (Aerospace & Advanced Tech)")
    st.success("**Primary Objective:** Secure private tender offer equity or high-value RSUs to dramatically accelerate financial independence.")
    
    st.markdown("#### Target Role Profile: Automation Controls / HIL Engineer")
    st.write("Leveraging the friction of rugged physical deployments to completely bypass traditional engineering degree filters.")
    
    st.divider()
    
    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
    metrics_col1.metric("Base Compensation Pivot", "$115k - $135k+", "Tier II Equivalent")
    metrics_col2.metric("Primary Wealth Vehicle", "Company Equity", "RSUs / Private Stock")
    metrics_col3.metric("Execution Timeline", "Month 24", "Post-Crucible")

# --- TAB 3: Independent Business ---
with tab3:
    st.markdown("### The Integrator Empire (Shenzhen Arbitrage)")
    st.warning("**Primary Objective:** Build an independent B2B Robotics Integration firm operating on a strict, debt-free cash flow model.")
    
    st.markdown("""
    By leveraging foundational business administration mechanics, alongside native-level Mandarin fluency and geographical familiarity with the Guangdong manufacturing hub, the traditional US supply chain middleman is bypassed for maximum margin.
    """)
    
    st.divider()
    
    st.markdown("#### The 50/40/10 Hardware Cash Flow Model")
    
    # Financial Data for Plotly Chart
    data = {
        "Project Phase": ["1. Down Payment (Signing)", "2. FAT (Factory Acceptance)", "3. SAT (Site Acceptance)"],
        "Capital Percentage": [50, 40, 10],
        "Cash Allocation ($)": [42500, 34000, 8500],
        "Operational Purpose": ["Hardware Sourcing & Freight", "Software Labor & Staging", "Pure System Profit"]
    }
    df = pd.DataFrame(data)
    
    # Plotly Bar Chart
    fig = px.bar(
        df, 
        x="Project Phase", 
        y="Capital Percentage", 
        text="Cash Allocation ($)", 
        color="Project Phase", 
        title="Standard $85k Turnkey Cell Revenue Structure",
        color_discrete_sequence=["#1E3A8A", "#3B82F6", "#93C5FD"]
    )
    fig.update_traces(texttemplate='$%{text:,}', textposition='outside')
    fig.update_layout(yaxis_range=[0, 60], showlegend=False)
    
    st.plotly_chart(fig, use_container_width=True)
