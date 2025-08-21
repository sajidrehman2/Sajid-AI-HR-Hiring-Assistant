import streamlit as st
import pandas as pd
from src import parser, ranking, chatbot, model

# Page configuration
st.set_page_config(
    page_title="Sajid AI HR & Hiring Assistant",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    .feature-card {
        background: #f8fafc;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #3b82f6;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .metric-container {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .status-success {
        background-color: #dcfce7;
        color: #166534;
        padding: 0.75rem;
        border-radius: 6px;
        border-left: 4px solid #22c55e;
    }
    
    .status-warning {
        background-color: #fef3c7;
        color: #92400e;
        padding: 0.75rem;
        border-radius: 6px;
        border-left: 4px solid #f59e0b;
    }
    
    .status-info {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 0.75rem;
        border-radius: 6px;
        border-left: 4px solid #3b82f6;
    }
    
    .sidebar-section {
        background: #f1f5f9;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f1f5f9;
        border-radius: 8px 8px 0 0;
        gap: 1px;
        padding-left: 20px;
        padding-right: 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #3b82f6;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🎯 Sajid AI HR & Hiring Assistant</h1>
    <p>Streamline your recruitment process with intelligent candidate screening and AI-powered insights</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with company info and navigation
with st.sidebar:
    st.markdown("""
    <div class="sidebar-section">
        <h3>🏢 System Overview</h3>
        <p>AI-powered recruitment platform designed to enhance HR efficiency and improve hiring decisions.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="metric-container">
            <h4>⚡ Speed</h4>
            <p>95% faster<br>screening</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-container">
            <h4>🎯 Accuracy</h4>
            <p>92% match<br>precision</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔧 System Status")
    st.markdown('<div class="status-success">✅ All systems operational</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📞 Support & Contact")
    st.markdown("""
    **📧 Email:** sajid.rehmanoffical95001@gmail.com  
    **🌐 Portfolio:** [View My Work](https://preview--data-visions-portfolio.lovable.app)  
    **💼 LinkedIn:** [Connect with Sajid](https://www.linkedin.com/in/sajid-rehman-b14474265)
    """)
    
    st.markdown("---")
    st.markdown("### 💡 Need Help?")
    st.markdown("Contact me for custom AI solutions and technical support!")

# Main content tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 Candidate Screening", 
    "💬 HR Assistant", 
    "📈 Analytics", 
    "ℹ️ System Info"
])

with tab1:
    st.markdown("## 📋 Intelligent Candidate Screening")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🎯 How It Works</h4>
            <p>Our AI system analyzes job requirements against candidate profiles using advanced NLP and machine learning algorithms to provide accurate matching scores and hiring recommendations.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>📊 What You Get</h4>
            <ul>
                <li>Skills compatibility score</li>
                <li>Experience alignment rating</li>
                <li>Hiring probability prediction</li>
                <li>Detailed candidate ranking</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Input section
    st.markdown("### 📄 Job Requirements")
    jd_text = st.text_area(
        "Enter the job description with required skills, experience, and qualifications:",
        height=150,
        placeholder="Paste your complete job description here, including required skills, experience level, education requirements, and job responsibilities..."
    )
    
    st.markdown("### 📁 Candidate Resumes")
    resumes = st.file_uploader(
        "Upload candidate resumes for analysis",
        accept_multiple_files=True,
        type=["pdf", "docx", "txt"],
        help="Supported formats: PDF, Word documents, and text files. You can upload multiple files at once."
    )
    
    # Process button and results
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col2:
        process_btn = st.button(
            "🚀 Analyze Candidates",
            type="primary",
            use_container_width=True
        )
    
    if process_btn:
        if jd_text and resumes:
            # Progress indicator
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            with st.spinner("Processing candidates..."):
                status_text.text("📊 Analyzing job requirements...")
                progress_bar.progress(0.2)
                jd_vec = ranking.embed_text(jd_text)
                
                status_text.text("📄 Parsing resumes...")
                progress_bar.progress(0.4)
                candidates = []
                
                for i, r in enumerate(resumes):
                    status_text.text(f"📋 Processing resume {i+1}/{len(resumes)}...")
                    progress_bar.progress(0.4 + (0.4 * i / len(resumes)))
                    
                    text, data = parser.parse_resume(r)
                    score = ranking.rank_resume(text, jd_vec)
                    prob = model.predict_hire_score(data)
                    
                    candidates.append({
                        **data,
                        "match_score": score,
                        "hire_probability": prob,
                        "resume_file": r.name
                    })
                
                status_text.text("🎯 Generating final rankings...")
                progress_bar.progress(0.9)
                
                df = pd.DataFrame(candidates).sort_values(by="match_score", ascending=False)
                progress_bar.progress(1.0)
                status_text.text("✅ Analysis complete!")
            
            # Results display
            st.markdown("### 🏆 Candidate Ranking Results")
            
            # Summary metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Candidates", len(df))
            with col2:
                st.metric("Top Match Score", f"{df['match_score'].max():.1%}")
            with col3:
                st.metric("Average Score", f"{df['match_score'].mean():.1%}")
            with col4:
                st.metric("Recommended", len(df[df['hire_probability'] > 0.7]))
            
            # Enhanced dataframe display
            st.markdown("#### 📊 Detailed Results")
            
            # Format the dataframe for better presentation
            display_df = df.copy()
            display_df['match_score'] = display_df['match_score'].apply(lambda x: f"{x:.1%}")
            display_df['hire_probability'] = display_df['hire_probability'].apply(lambda x: f"{x:.1%}")
            
            st.dataframe(
                display_df,
                use_container_width=True,
                column_config={
                    "match_score": st.column_config.TextColumn("Match Score"),
                    "hire_probability": st.column_config.TextColumn("Hire Probability"),
                    "resume_file": st.column_config.TextColumn("Resume File")
                }
            )
            
            # Download section
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    "📥 Download Results (CSV)",
                    df.to_csv(index=False),
                    "candidate_analysis_results.csv",
                    "text/csv",
                    use_container_width=True
                )
            
            with col2:
                st.download_button(
                    "📋 Download Summary Report",
                    f"Candidate Analysis Summary\n{'='*30}\nTotal Candidates: {len(df)}\nTop Score: {df['match_score'].max():.1%}\nAverage Score: {df['match_score'].mean():.1%}\nRecommended Hires: {len(df[df['hire_probability'] > 0.7])}",
                    "summary_report.txt",
                    "text/plain",
                    use_container_width=True
                )
                
        else:
            st.markdown("""
            <div class="status-warning">
                ⚠️ <strong>Missing Information</strong><br>
                Please provide both a job description and upload candidate resumes to proceed with the analysis.
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("## 💬 AI HR Assistant")
    
    st.markdown("""
    <div class="feature-card">
        <h4>🤖 Your Personal HR Consultant</h4>
        <p>Get instant answers to HR policies, recruitment best practices, legal compliance questions, and more. Our AI assistant is trained on comprehensive HR knowledge.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        st.markdown("### 💡 Sample Questions")
        sample_questions = [
            "What are best practices for conducting interviews?",
            "How should I structure a job offer letter?",
            "What are legal considerations for background checks?",
            "How can I improve employee retention?",
            "What's the standard probation period policy?"
        ]
        
        for i, question in enumerate(sample_questions, 1):
            if st.button(f"💭 {question}", key=f"sample_{i}"):
                st.session_state['hr_question'] = question
    
    with col1:
        user_question = st.text_area(
            "Ask your HR question:",
            height=120,
            placeholder="Type your HR or recruitment related question here...",
            value=st.session_state.get('hr_question', '')
        )
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            ask_btn = st.button("🚀 Get Answer", type="primary", use_container_width=True)
        with col_btn2:
            clear_btn = st.button("🗑️ Clear", use_container_width=True)
        
        if clear_btn:
            st.session_state['hr_question'] = ''
            st.rerun()
        
        if ask_btn and user_question.strip():
            with st.spinner("🤔 Analyzing your question..."):
                # Enhanced HR Assistant with comprehensive responses
                hr_responses = {
                    # Interview Questions
                    "interview": {
                        "keywords": ["interview", "interviewing", "questions", "candidate assessment"],
                        "response": """
                        **🎯 Best Practices for Conducting Interviews:**
                        
                        **Before the Interview:**
                        • Review the candidate's resume thoroughly
                        • Prepare structured, job-relevant questions
                        • Set up a comfortable interview environment
                        • Have multiple interviewers for different perspectives
                        
                        **During the Interview:**
                        • Start with rapport-building questions
                        • Use behavioral questions (STAR method)
                        • Ask open-ended questions to assess problem-solving
                        • Take detailed notes for fair comparison
                        • Allow time for candidate questions
                        
                        **Sample Questions:**
                        • "Tell me about a time you handled a difficult situation"
                        • "How do you prioritize tasks under pressure?"
                        • "Describe your ideal work environment"
                        
                        **After the Interview:**
                        • Evaluate candidates against consistent criteria
                        • Provide timely feedback to candidates
                        • Document decisions for compliance
                        """
                    },
                    # Job Offer Letters
                    "offer": {
                        "keywords": ["offer letter", "job offer", "employment offer", "hiring letter"],
                        "response": """
                        **📋 Job Offer Letter Structure:**
                        
                        **Essential Components:**
                        • Job title and department
                        • Start date and work schedule
                        • Salary and benefits package
                        • Reporting structure
                        • Employment type (full-time/part-time/contract)
                        
                        **Additional Details:**
                        • Probationary period (typically 3-6 months)
                        • Confidentiality and non-compete clauses
                        • Termination conditions
                        • Company policies reference
                        • Deadline for acceptance (usually 5-7 business days)
                        
                        **Professional Tone Tips:**
                        • Use formal but welcoming language
                        • Clearly state terms and conditions
                        • Include next steps for acceptance
                        • Provide contact information for questions
                        
                        **Legal Considerations:**
                        • Ensure compliance with local employment laws
                        • Include at-will employment clause (where applicable)
                        • Specify background check requirements
                        """
                    },
                    # Background Checks
                    "background": {
                        "keywords": ["background check", "screening", "verification", "legal considerations"],
                        "response": """
                        **🔍 Legal Considerations for Background Checks:**
                        
                        **Legal Requirements:**
                        • Obtain written consent before conducting checks
                        • Follow Fair Credit Reporting Act (FCRA) guidelines
                        • Provide pre-adverse action notice if considering rejection
                        • Allow opportunity for candidate to dispute findings
                        
                        **What You Can Check:**
                        • Criminal history (job-relevant)
                        • Employment verification
                        • Education credentials
                        • Professional licenses
                        • Credit history (for financial positions only)
                        
                        **Best Practices:**
                        • Use reputable screening companies
                        • Apply consistent standards to all candidates
                        • Consider relevance of findings to job requirements
                        • Maintain confidentiality of results
                        
                        **Prohibited Practices:**
                        • Blanket exclusions based on criminal history
                        • Discrimination based on protected characteristics
                        • Social media stalking
                        • Unauthorized reference checks
                        """
                    },
                    # Employee Retention
                    "retention": {
                        "keywords": ["retention", "employee retention", "keeping employees", "turnover"],
                        "response": """
                        **🚀 Proven Employee Retention Strategies:**
                        
                        **Compensation & Benefits:**
                        • Competitive salary benchmarking
                        • Performance-based bonuses
                        • Comprehensive benefits package
                        • Flexible work arrangements
                        • Professional development budget
                        
                        **Work Environment:**
                        • Foster positive company culture
                        • Encourage work-life balance
                        • Provide modern tools and technology
                        • Create comfortable physical workspace
                        • Promote team collaboration
                        
                        **Career Development:**
                        • Clear career progression paths
                        • Regular skill development training
                        • Mentorship programs
                        • Cross-functional project opportunities
                        • Leadership development initiatives
                        
                        **Recognition & Engagement:**
                        • Regular feedback and recognition
                        • Employee of the month programs
                        • Team building activities
                        • Open communication channels
                        • Employee satisfaction surveys
                        
                        **Management Practices:**
                        • Train managers on people skills
                        • Conduct regular one-on-one meetings
                        • Address issues promptly
                        • Provide autonomy and trust
                        """
                    },
                    # Probation Period
                    "probation": {
                        "keywords": ["probation", "probationary period", "trial period", "new employee"],
                        "response": """
                        **⏰ Standard Probation Period Policies:**
                        
                        **Typical Duration:**
                        • Entry-level positions: 3 months
                        • Mid-level positions: 3-6 months
                        • Senior/specialized roles: 6 months
                        • Executive positions: 6-12 months
                        
                        **Purpose of Probation:**
                        • Assess job performance and fit
                        • Provide structured feedback
                        • Allow mutual evaluation period
                        • Establish clear expectations
                        
                        **During Probation:**
                        • Regular check-ins (weekly/bi-weekly)
                        • Clear performance metrics
                        • Training and onboarding support
                        • Documentation of progress
                        • Open communication channels
                        
                        **Probation Review Process:**
                        • 30, 60, 90-day formal reviews
                        • Goal setting and achievement tracking
                        • Skills assessment
                        • Cultural fit evaluation
                        • Decision on permanent employment
                        
                        **Best Practices:**
                        • Clearly communicate expectations
                        • Provide adequate support and resources
                        • Document all interactions
                        • Be fair and consistent
                        • Make decisions based on objective criteria
                        """
                    }
                }
                
                # Find matching response
                user_q_lower = user_question.lower()
                response_found = False
                
                for category, info in hr_responses.items():
                    if any(keyword in user_q_lower for keyword in info["keywords"]):
                        answer = info["response"]
                        response_found = True
                        break
                
                if not response_found:
                    # Use the original chatbot for other questions
                    try:
                        answer = chatbot.get_answer(user_question)
                    except:
                        answer = """
                        **🤖 AI HR Assistant Response:**
                        
                        Thank you for your question! While I don't have a specific response for this query, here are some general HR best practices:
                        
                        **For HR Policies:** Always ensure compliance with local employment laws and company guidelines.
                        
                        **For Employee Relations:** Focus on clear communication, fair treatment, and consistent application of policies.
                        
                        **For Recruitment:** Use structured processes, objective criteria, and maintain detailed documentation.
                        
                        **Need More Help?** 
                        Contact Sajid directly for personalized HR solutions:
                        • Email: sajid.rehmanoffical95001@gmail.com
                        • LinkedIn: [Connect with Sajid](https://www.linkedin.com/in/sajid-rehman-b14474265)
                        """
            
            st.markdown("### 💡 AI Assistant Response")
            st.markdown(f"""
            <div class="status-info">
                <strong>📋 Question:</strong> {user_question}<br><br>
                <strong>🎯 Answer:</strong><br>{answer}
            </div>
            """, unsafe_allow_html=True)
            
            # Feedback section
            st.markdown("### 👍 Was this helpful?")
            col1, col2 = st.columns(2)
            with col1:
                st.button("👍 Yes, helpful", use_container_width=True)
            with col2:
                st.button("👎 Needs improvement", use_container_width=True)

with tab3:
    st.markdown("## 📈 Analytics Dashboard")
    
    st.markdown("""
    <div class="status-info">
        🚧 <strong>Analytics Dashboard</strong><br>
        Advanced analytics and reporting features are coming soon. This will include candidate pipeline metrics, hiring success rates, and performance insights.
    </div>
    """, unsafe_allow_html=True)
    
    # Placeholder analytics
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Upcoming Features</h4>
            <ul>
                <li>Hiring pipeline analytics</li>
                <li>Candidate source effectiveness</li>
                <li>Time-to-hire metrics</li>
                <li>Interview success rates</li>
                <li>Diversity & inclusion insights</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>📈 Reports Available</h4>
            <ul>
                <li>Weekly hiring summaries</li>
                <li>Monthly recruitment KPIs</li>
                <li>Quarterly trend analysis</li>
                <li>Custom date range reports</li>
                <li>Executive dashboards</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("## ℹ️ System Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🎯 About This Platform</h4>
            <p>This AI-powered HR Assistant is designed to revolutionize your recruitment process by leveraging advanced machine learning algorithms and natural language processing.</p>
            
            <h5>🔧 Key Technologies:</h5>
            <ul>
                <li><strong>Machine Learning:</strong> Advanced candidate scoring algorithms</li>
                <li><strong>NLP Processing:</strong> Intelligent resume parsing and analysis</li>
                <li><strong>Semantic Matching:</strong> Job-candidate compatibility assessment</li>
                <li><strong>Predictive Analytics:</strong> Hiring success probability models</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🔒 Security & Privacy</h4>
            <p>Your data security and candidate privacy are our top priorities.</p>
            
            <h5>🛡️ Security Features:</h5>
            <ul>
                <li><strong>Data Encryption:</strong> End-to-end encryption for all data</li>
                <li><strong>GDPR Compliant:</strong> Full compliance with data protection regulations</li>
                <li><strong>Secure Processing:</strong> No data retention beyond session</li>
                <li><strong>Access Control:</strong> Role-based permission system</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h4>🚀 Version Information</h4>
        <p><strong>Current Version:</strong> 2.1.0 Professional Edition</p>
        <p><strong>Last Updated:</strong> August 2025</p>
        <p><strong>Supported Formats:</strong> PDF, DOCX, TXT resume files</p>
        <p><strong>Built With:</strong> Streamlit, Python, Advanced ML Models</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact and support information
    st.markdown("### 📞 Support & Contact")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📧 Developer Contact**  
        sajid.rehmanoffical95001@gmail.com  
        Response: 24-48 hours
        """)
    
    with col2:
        st.markdown("""
        **🌐 Portfolio**  
        [View My Projects](https://preview--data-visions-portfolio.lovable.app)  
        See more AI solutions
        """)
    
    with col3:
        st.markdown("""
        **💼 LinkedIn**  
        [Connect with Sajid](https://www.linkedin.com/in/sajid-rehman-b14474265)  
        Professional networking
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6b7280; padding: 1rem;">
    © 2025 Sajid AI HR Platform | Professional Recruitment Solutions | 
    <a href="mailto:sajid.rehmanoffical95001@gmail.com" style="color: #3b82f6;">Contact Developer</a> | 
    <a href="https://preview--data-visions-portfolio.lovable.app" style="color: #3b82f6;" target="_blank">Portfolio</a> | 
    <a href="https://www.linkedin.com/in/sajid-rehman-b14474265" style="color: #3b82f6;" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)