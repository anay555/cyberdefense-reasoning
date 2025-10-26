import streamlit as st
import json
import time
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="CyberDefense Reasoning",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    color: #FF6B6B;
    text-align: center;
    margin-bottom: 2rem;
}
.sub-header {
    font-size: 1.5rem;
    color: #4ECDC4;
    margin-bottom: 1rem;
}
.threat-box {
    background-color: #f0f2f6;
    padding: 1rem;
    border-radius: 10px;
    border-left: 5px solid #FF6B6B;
    margin: 1rem 0;
}
.reasoning-box {
    background-color: #e8f4fd;
    padding: 1rem;
    border-radius: 10px;
    border-left: 5px solid #4ECDC4;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# Sample threat scenarios for demo
THREAT_SCENARIOS = {
    "Phishing Email Campaign": {
        "description": "Suspicious email with malicious attachment targeting finance department",
        "indicators": ["Sender: noreply@bank-secure.net", "Attachment: invoice_urgent.exe", "Urgency language used"],
        "adversarial_reasoning": "The attacker chose a finance-themed phishing email because: 1) Finance departments handle sensitive data, 2) Urgency creates pressure to bypass security protocols, 3) .exe disguised as invoice exploits trust in routine business documents",
        "mitigation": "Implement email filtering, user training, and attachment sandboxing"
    },
    "Lateral Movement Detected": {
        "description": "Unusual network traffic between compromised workstation and domain controller",
        "indicators": ["Source: 192.168.1.45", "Destination: DC01 (192.168.1.10)", "Protocol: SMB unusual hours"],
        "adversarial_reasoning": "The attacker is moving laterally because: 1) Initial compromise was a low-privilege workstation, 2) Domain controller access provides administrative control, 3) SMB protocol allows credential harvesting and privilege escalation",
        "mitigation": "Isolate affected systems, reset domain credentials, implement network segmentation"
    },
    "Data Exfiltration Attempt": {
        "description": "Large file transfer to external cloud storage during off-hours",
        "indicators": ["Volume: 2.5GB", "Destination: dropbox.com", "Time: 2:30 AM", "User: admin_backup"],
        "adversarial_reasoning": "The attacker chose this exfiltration method because: 1) Off-hours reduce detection probability, 2) Cloud storage appears legitimate, 3) Admin account provides access justification, 4) Large volume suggests valuable data theft",
        "mitigation": "Block unauthorized cloud services, implement DLP policies, monitor admin account usage"
    }
}

def simulate_ai_reasoning(scenario_data):
    """Simulate AI processing for adversarial reasoning"""
    with st.spinner("🤖 AI analyzing attacker psychology and motivations..."):
        time.sleep(2)  # Simulate processing time
    
    return {
        "confidence": 0.87,
        "risk_level": "HIGH",
        "reasoning": scenario_data["adversarial_reasoning"],
        "recommendations": scenario_data["mitigation"]
    }

def main():
    # Header
    st.markdown('<h1 class="main-header">🛡️ CyberDefense Reasoning</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI-Powered Adversarial Threat Analysis</p>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("⚙️ Control Panel")
    st.sidebar.markdown("---")
    
    # Mode selection
    mode = st.sidebar.selectbox(
        "Analysis Mode",
        ["Threat Investigation", "Live Monitoring", "Historical Analysis"]
    )
    
    if mode == "Threat Investigation":
        st.markdown('<h2 class="sub-header">🔍 Threat Investigation Mode</h2>', unsafe_allow_html=True)
        
        # Scenario selection
        scenario_name = st.selectbox(
            "Select Threat Scenario",
            list(THREAT_SCENARIOS.keys())
        )
        
        scenario = THREAT_SCENARIOS[scenario_name]
        
        # Display threat information
        st.markdown('<div class="threat-box">', unsafe_allow_html=True)
        st.markdown(f"**📋 Threat Description:** {scenario['description']}")
        st.markdown("**🔍 Key Indicators:**")
        for indicator in scenario['indicators']:
            st.markdown(f"• {indicator}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Analyze button
        if st.button("🚀 Run Adversarial Analysis", type="primary"):
            analysis = simulate_ai_reasoning(scenario)
            
            # Display results
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("AI Confidence", f"{analysis['confidence']:.0%}")
            with col2:
                st.metric("Risk Level", analysis['risk_level'])
            with col3:
                st.metric("Analysis Time", "2.3s")
            
            # Adversarial reasoning
            st.markdown('<div class="reasoning-box">', unsafe_allow_html=True)
            st.markdown("**🧠 Adversarial Reasoning Analysis:**")
            st.write(analysis['reasoning'])
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Recommendations
            st.markdown("**🛡️ Recommended Actions:**")
            st.info(analysis['recommendations'])
            
            # Timeline simulation
            st.markdown("**⏱️ Attack Timeline Reconstruction:**")
            timeline_data = {
                "Time": ["T-30min", "T-15min", "T-5min", "T-0min", "T+10min"],
                "Attacker Action": [
                    "Reconnaissance", 
                    "Initial Access", 
                    "Persistence", 
                    "Privilege Escalation", 
                    "Data Access"
                ],
                "System Response": [
                    "Normal", 
                    "Alert Generated", 
                    "Suspicious Activity", 
                    "Critical Alert", 
                    "Investigation Started"
                ]
            }
            st.dataframe(pd.DataFrame(timeline_data), use_container_width=True)
    
    elif mode == "Live Monitoring":
        st.markdown('<h2 class="sub-header">📡 Live Monitoring Dashboard</h2>', unsafe_allow_html=True)
        
        # Real-time metrics (simulated)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Active Threats", "3", "↑1")
        with col2:
            st.metric("Analysis Speed", "1.2s", "↓0.3s")
        with col3:
            st.metric("Accuracy Rate", "94.2%", "↑2.1%")
        with col4:
            st.metric("Threats Blocked", "127", "↑15")
        
        # Live feed simulation
        st.markdown("**🔴 Live Threat Feed:**")
        threat_feed = st.empty()
        
        if st.button("Start Live Monitoring"):
            for i in range(5):
                current_time = datetime.now().strftime("%H:%M:%S")
                threat_feed.info(f"[{current_time}] Analyzing network traffic... Adversarial pattern detected in sector {i+1}")
                time.sleep(1)
    
    else:  # Historical Analysis
        st.markdown('<h2 class="sub-header">📊 Historical Threat Analysis</h2>', unsafe_allow_html=True)
        
        # Sample historical data
        hist_data = {
            "Date": pd.date_range(start="2024-10-01", end="2024-10-26", freq="D"),
            "Threats Detected": [5, 8, 12, 3, 15, 7, 9, 11, 6, 14, 4, 13, 8, 10, 16, 5, 7, 9, 12, 6, 8, 11, 13, 7, 9, 4]
        }
        
        df = pd.DataFrame(hist_data)
        st.line_chart(df.set_index("Date"))
        
        st.markdown("**📈 Trend Analysis:**")
        st.info("AI has identified a 23% increase in sophisticated attacks over the past week, with adversaries adapting to previous countermeasures.")

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "🚀 Built for K2 Think Hackathon | Powered by Advanced AI Adversarial Reasoning"
        "</div>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()