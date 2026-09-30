import os
import sys
import time
import requests
import streamlit as st


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from backend.config import BACKEND_URL


st.set_page_config(
    page_title="CareerCraft AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');


html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 80% 5%,
            rgba(99,102,241,0.10),
            transparent 28%
        ),
        radial-gradient(
            circle at 10% 20%,
            rgba(139,92,246,0.07),
            transparent 25%
        ),
        #0b0d12;
}


.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1450px;
}


section[data-testid="stSidebar"] {
    background: #10131a;
    border-right: 1px solid rgba(255,255,255,0.07);
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}


.sidebar-brand {
    padding: 10px 8px 25px 8px;
}

.sidebar-brand-title {
    font-size: 23px;
    font-weight: 800;
    letter-spacing: -0.7px;
}

.sidebar-brand-title span {
    color: #8b5cf6;
}

.sidebar-brand-subtitle {
    color: #858b99;
    font-size: 12px;
    margin-top: 5px;
}


.hero {
    padding: 12px 0 30px 0;
}

.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(139,92,246,0.10);
    border: 1px solid rgba(139,92,246,0.22);
    color: #b7a1ff;
    padding: 7px 12px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 18px;
}

.hero-title {
    font-size: clamp(42px, 5vw, 64px);
    line-height: 1.02;
    letter-spacing: -2.8px;
    font-weight: 800;
    margin: 0;
    color: #f5f7fb;
}

.hero-title span {
    background: linear-gradient(
        90deg,
        #a78bfa,
        #c4b5fd,
        #818cf8
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-description {
    color: #949baa;
    font-size: 16px;
    line-height: 1.7;
    max-width: 720px;
    margin-top: 15px;
}


.card {
    background: rgba(20,23,31,0.88);
    border: 1px solid rgba(255,255,255,0.075);
    border-radius: 18px;
    padding: 22px;
    transition: all 0.25s ease;
}

.card:hover {
    border-color: rgba(139,92,246,0.30);
    transform: translateY(-2px);
    box-shadow: 0 15px 45px rgba(0,0,0,0.20);
}

.card-title {
    font-size: 15px;
    font-weight: 700;
    color: #f3f4f6;
    margin-bottom: 5px;
}

.card-subtitle {
    font-size: 12px;
    color: #7e8594;
}


.metric-card {
    position: relative;
    overflow: hidden;
    background: linear-gradient(
        145deg,
        rgba(24,27,37,0.96),
        rgba(17,19,26,0.96)
    );
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 18px;
    padding: 20px;
    min-height: 130px;
}

.metric-card::after {
    content: "";
    position: absolute;
    width: 90px;
    height: 90px;
    right: -30px;
    top: -30px;
    background: rgba(139,92,246,0.12);
    border-radius: 50%;
    filter: blur(5px);
}

.metric-label {
    color: #8d94a2;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.7px;
}

.metric-value {
    color: #f8fafc;
    font-size: 34px;
    font-weight: 800;
    margin-top: 10px;
    letter-spacing: -1px;
}

.metric-caption {
    color: #737b8b;
    font-size: 11px;
    margin-top: 3px;
}


.stButton > button {
    border-radius: 12px !important;
    border: 1px solid rgba(139,92,246,0.30) !important;
    background: linear-gradient(
        135deg,
        #7c3aed,
        #8b5cf6
    ) !important;
    color: white !important;
    font-weight: 700 !important;
    min-height: 45px;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(124,58,237,0.28);
}


button[kind="secondary"] {
    background: #171a22 !important;
}


.stTextArea textarea,
.stTextInput input {
    background: #11141b !important;
    color: #eef0f5 !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 13px !important;
}

.stTextArea textarea:focus,
.stTextInput input:focus {
    border-color: rgba(139,92,246,0.7) !important;
    box-shadow: 0 0 0 2px rgba(139,92,246,0.10) !important;
}


[data-testid="stFileUploader"] {
    background: #11141b;
    border-radius: 15px;
}


.stTabs [data-baseweb="tab-list"] {
    gap: 5px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

.stTabs [data-baseweb="tab"] {
    padding: 12px 16px;
    color: #858b99;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    color: #c4b5fd !important;
}


.success-box {
    background: rgba(34,197,94,0.08);
    border: 1px solid rgba(34,197,94,0.18);
    color: #86efac;
    padding: 13px 16px;
    border-radius: 12px;
    font-size: 13px;
}

.info-box {
    background: rgba(99,102,241,0.08);
    border: 1px solid rgba(99,102,241,0.18);
    color: #c7d2fe;
    padding: 13px 16px;
    border-radius: 12px;
    font-size: 13px;
}


.skill-pill {
    display: inline-block;
    background: rgba(139,92,246,0.10);
    border: 1px solid rgba(139,92,246,0.20);
    color: #c4b5fd;
    padding: 6px 10px;
    border-radius: 20px;
    margin: 3px;
    font-size: 12px;
}

.missing-pill {
    display: inline-block;
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.17);
    color: #fca5a5;
    padding: 6px 10px;
    border-radius: 20px;
    margin: 3px;
    font-size: 12px;
}


.processing {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 17px;
    background: #11141b;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    margin: 12px 0;
}

.processing-dot {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: #8b5cf6;
    box-shadow:
        0 0 0 0 rgba(139,92,246,0.6);
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 rgba(139,92,246,0.6);
    }
    70% {
        box-shadow: 0 0 0 10px rgba(139,92,246,0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(139,92,246,0);
    }
}


.footer {
    text-align: center;
    color: #555d6d;
    font-size: 11px;
    padding: 45px 0 10px 0;
}

</style>
""",
    unsafe_allow_html=True,
)


if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "uploaded_name" not in st.session_state:
    st.session_state.uploaded_name = None


def safe_get(obj, key, default=None):
    if isinstance(obj, dict):
        return obj.get(key, default)
    return default


def list_value(value):
    if value is None:
        return []

    if isinstance(value, list):
        return value

    return [value]


def render_skill_pills(skills, missing=False):
    skills = list_value(skills)

    if not skills:
        st.caption("None identified")

        return

    html = ""

    for skill in skills:
        if missing:
            html += f'<span class="missing-pill">{skill}</span>'
        else:
            html += f'<span class="skill-pill">{skill}</span>'

    st.markdown(html, unsafe_allow_html=True)


def metric_card(label, value, caption=""):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-caption">{caption}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def processing_message(message):
    st.markdown(
        f"""
        <div class="processing">
            <div class="processing-dot"></div>
            <div>{message}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def extract_score(obj, key, default=0):
    value = safe_get(obj, key, default)

    try:
        return int(float(value))
    except Exception:
        return default


with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="sidebar-brand-title">
                Career<span>Craft</span> AI
            </div>
            <div class="sidebar-brand-subtitle">
                Resume intelligence for your next opportunity
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Your resume")

    uploaded_file = st.file_uploader(
        "Upload PDF, DOCX or TXT",
        type=["pdf", "docx", "txt"],
        label_visibility="collapsed",
    )

    if uploaded_file:
        st.markdown(
            f"""
            <div class="success-box">
                ✓ {uploaded_file.name}<br>
                <span style="opacity:.65">
                    {uploaded_file.size / 1024:.1f} KB · Ready
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### Knowledge base")

    try:
        rag_response = requests.get(
            f"{BACKEND_URL}/rag/status",
            timeout=10,
        )

        rag_data = rag_response.json()

        if rag_data.get("ready") or rag_data.get("status") in [
            "ready",
            "indexed",
        ]:
            st.markdown(
                """
                <div class="success-box">
                    ✓ Knowledge base connected
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div class="info-box">
                    Knowledge base available
                </div>
                """,
                unsafe_allow_html=True,
            )

    except Exception:
        st.caption("Knowledge base status unavailable")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "↻  Rebuild knowledge base",
        use_container_width=True,
    ):
        try:
            response = requests.post(
                f"{BACKEND_URL}/rag/ingest",
                timeout=120,
            )

            if response.ok:
                st.success("Knowledge base updated.")
                st.rerun()
            else:
                st.error("Could not rebuild the knowledge base.")

        except Exception as e:
            st.error(str(e))

st.markdown(
"""<div class="hero">
<div class="hero-eyebrow">✦ AI-powered career workspace</div>
<h1 class="hero-title">Make your resume<br><span>work harder.</span></h1>
<div class="hero-description">Understand how your experience aligns with a target role, discover skill gaps, and create a stronger application without changing the facts that make your resume yours.</div>
</div>""",
    unsafe_allow_html=True,
)


if st.session_state.analysis is None:

    st.markdown("### Start with a resume and a role")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:

        st.markdown(
            """
            <div class="card">
                <div class="card-title">📄 Your resume</div>
                <div class="card-subtitle">
                    Upload the version you want to improve.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if uploaded_file:
            st.markdown(
                f"""
                <div style="
                    margin-top:10px;
                    padding:14px;
                    background:#141821;
                    border:1px solid rgba(139,92,246,.20);
                    border-radius:12px;
                ">
                    <b>✓ {uploaded_file.name}</b>
                    <br>
                    <span style="color:#727989;font-size:12px;">
                        Resume ready for analysis
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:
            st.info("Upload your resume from the sidebar.")

    with col2:

        st.markdown(
            """
            <div class="card">
                <div class="card-title">💼 Target opportunity</div>
                <div class="card-subtitle">
                    Paste the job description you're applying for.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        job_description = st.text_area(
            "Job description",
            height=250,
            placeholder=(
                "Paste the job description here...\n\n"
                "Example:\n"
                "Looking for a Software Engineer with Python, "
                "FastAPI, SQL and experience building AI applications."
            ),
            label_visibility="collapsed",
        )

    st.markdown("<br>", unsafe_allow_html=True)

    analyze_clicked = st.button(
        "✦  Analyze my application",
        use_container_width=True,
    )

    if analyze_clicked:

        if uploaded_file is None:
            st.warning("Please upload your resume first.")

        elif not job_description.strip():
            st.warning("Please paste the job description.")

        else:

            progress = st.empty()

            stages = [
                "Reading your resume...",
                "Understanding the target role...",
                "Comparing your experience...",
                "Finding relevant guidance...",
                "Preparing your recommendations...",
            ]

            try:

                for stage in stages:
                    progress.markdown(
                        f"""
                        <div class="processing">
                            <div class="processing-dot"></div>
                            <div>{stage}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    time.sleep(0.25)

                response = requests.post(
                    f"{BACKEND_URL}/analyze",
                    files={
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            uploaded_file.type,
                        )
                    },
                    data={
                        "job_description": job_description,
                    },
                    timeout=300,
                )

                progress.empty()

                if response.ok:

                    st.session_state.analysis = response.json()
                    st.session_state.uploaded_name = uploaded_file.name

                    st.rerun()

                else:

                    try:
                        error = response.json().get(
                            "detail",
                            response.text,
                        )
                    except Exception:
                        error = response.text

                    st.error(
                        f"Analysis failed: {error}"
                    )

            except requests.exceptions.Timeout:

                progress.empty()

                st.error(
                    "The analysis took too long. "
                    "Please try again."
                )

            except Exception as e:

                progress.empty()

                st.error(str(e))


else:

    data = st.session_state.analysis

    resume = safe_get(data, "resume", {})
    job = safe_get(data, "job", {})
    match = safe_get(data, "match", {})
    ats = safe_get(data, "ats", {})
    skill_gap = safe_get(data, "skill_gap", {})


    role = (
        safe_get(job, "title")
        or safe_get(job, "role")
        or "Target role"
    )

    company = safe_get(job, "company", "")

    st.markdown(
f"""<div style="
display:flex;
justify-content:space-between;
align-items:flex-end;
margin-bottom:25px;
">
<div>
<div style="
color:#8b5cf6;
font-size:12px;
font-weight:700;
text-transform:uppercase;
letter-spacing:1px;
">
APPLICATION REVIEW
</div>

<div style="
font-size:32px;
font-weight:800;
letter-spacing:-1.2px;
margin-top:5px;
">
{role}
</div>

<div style="
color:#777f8e;
font-size:13px;
margin-top:4px;
">
{company if company else "Personalized resume analysis"}
</div>
</div>
</div>""",
unsafe_allow_html=True,
)


    alignment = extract_score(
        match,
        "alignment_score",
        safe_get(match, "score", 0),
    )

    ats_score = extract_score(
        ats,
        "score",
        safe_get(ats, "ats_score", 0),
    )

    matched = len(
        list_value(
            safe_get(match, "matched_skills", [])
        )
    )

    missing = len(
        list_value(
            safe_get(match, "missing_skills", [])
        )
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "Job alignment",
            f"{alignment}/100",
            "How closely your profile fits the role",
        )

    with c2:
        metric_card(
            "ATS readiness",
            f"{ats_score}/100",
            "Keyword and structure signals",
        )

    with c3:
        metric_card(
            "Matched skills",
            matched,
            "Skills found in both profiles",
        )

    with c4:
        metric_card(
            "Skill gaps",
            missing,
            "Potential areas to strengthen",
        )

    st.markdown("<br>", unsafe_allow_html=True)


    tabs = st.tabs(
        [
            "Overview",
            "Resume",
            "Job Match",
            "ATS",
            "Skill Gap",
            "Tailored Resume",
            "Cover Letter",
            "Interview",
            "Quality",
            "RAG Evidence",
            "Exports",
        ]
    )


    with tabs[0]:

        st.markdown("### Your application at a glance")

        left, right = st.columns([1.15, 0.85], gap="large")

        with left:

            st.markdown(
                """
                <div class="card">
                    <div class="card-title">
                        What stands out
                    </div>
                    <div class="card-subtitle">
                        Key signals from your resume and the target role.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            matched_skills = safe_get(
                match,
                "matched_skills",
                [],
            )

            if matched_skills:

                st.markdown("#### Strong matches")

                render_skill_pills(
                    matched_skills
                )

            else:

                st.info(
                    "No direct skill matches were detected."
                )

            st.markdown("#### Areas to strengthen")

            render_skill_pills(
                safe_get(
                    match,
                    "missing_skills",
                    [],
                ),
                missing=True,
            )

        with right:

            st.markdown(
                """
                <div class="card">
                    <div class="card-title">
                        Analysis summary
                    </div>
                    <div class="card-subtitle">
                        A quick view before diving deeper.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.progress(
                min(max(alignment / 100, 0), 1),
                text=f"Job alignment · {alignment}%",
            )

            st.progress(
                min(max(ats_score / 100, 0), 1),
                text=f"ATS readiness · {ats_score}%",
            )

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(
                """
                <div class="info-box">
                    Your recommendations are based on the
                    information found in your resume and the
                    requirements of the target role.
                </div>
                """,
                unsafe_allow_html=True,
            )


    with tabs[1]:

        st.markdown("### Resume profile")

        summary = safe_get(
            resume,
            "summary",
            "",
        )

        if summary:

            st.markdown(
                f"""
                <div class="card">
                    <div class="card-title">
                        Professional summary
                    </div>
                    <div style="
                        color:#a8afbd;
                        line-height:1.7;
                        margin-top:10px;
                    ">
                        {summary}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        skills = safe_get(
            resume,
            "skills",
            {},
        )

        if skills:

            st.markdown("#### Skills detected")

            skill_columns = st.columns(3)

            categories = [
                ("Technical", "technical"),
                ("Tools", "tools"),
                ("Frameworks", "frameworks"),
            ]

            for column, (label, key) in zip(
                skill_columns,
                categories,
            ):

                with column:

                    st.markdown(
                        f"**{label}**"
                    )

                    render_skill_pills(
                        safe_get(
                            skills,
                            key,
                            [],
                        )
                    )


    with tabs[2]:

        st.markdown("### Job match")

        st.markdown(
            """
            <div class="info-box">
                This section explains where your existing
                experience overlaps with the opportunity.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("#### Matched skills")

        render_skill_pills(
            safe_get(
                match,
                "matched_skills",
                [],
            )
        )

        st.markdown("#### Missing skills")

        render_skill_pills(
            safe_get(
                match,
                "missing_skills",
                [],
            ),
            missing=True,
        )

        partial = safe_get(
            match,
            "partial_matches",
            [],
        )

        if partial:

            st.markdown("#### Partial matches")

            render_skill_pills(
                partial
            )


    with tabs[3]:

        st.markdown("### ATS readiness")

        st.progress(
            min(max(ats_score / 100, 0), 1),
            text=f"{ats_score}/100",
        )

        for section in [
            "strengths",
            "weaknesses",
            "missing_keywords",
            "suggested_improvements",
        ]:

            values = safe_get(
                ats,
                section,
                [],
            )

            if values:

                st.markdown(
                    f"#### {section.replace('_', ' ').title()}"
                )

                for item in list_value(values):

                    st.markdown(
                        f"""
                        <div class="card"
                             style="margin-bottom:8px;">
                            {item}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )


    with tabs[4]:

        st.markdown("### Skill gap analysis")

        strong = safe_get(
            skill_gap,
            "strong",
            [],
        )

        partial = safe_get(
            skill_gap,
            "partial",
            [],
        )

        missing_skills = safe_get(
            skill_gap,
            "missing",
            [],
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown("#### Strong")

            render_skill_pills(strong)

        with col2:

            st.markdown("#### Partial")

            render_skill_pills(partial)

        with col3:

            st.markdown("#### Missing")

            render_skill_pills(
                missing_skills,
                missing=True,
            )

        priorities = safe_get(
            skill_gap,
            "learning_priorities",
            [],
        )

        if priorities:

            st.markdown("### Suggested learning priorities")

            for i, skill in enumerate(
                priorities,
                start=1,
            ):

                st.markdown(
                    f"""
                    <div class="card"
                         style="margin-bottom:8px;">

                        <span style="
                            color:#8b5cf6;
                            font-weight:800;
                        ">
                            {i:02}
                        </span>

                        &nbsp;&nbsp;

                        {skill}

                    </div>
                    """,
                    unsafe_allow_html=True,
                )


    with tabs[5]:

        st.markdown("### Tailored resume")

        optimized = safe_get(
            data,
            "optimized_resume",
            {},
        )

        if optimized:

            st.success(
                "Your resume has been tailored to the target opportunity while preserving the information from your original resume."
            )

            for key, value in optimized.items():

                if value:

                    title = key.replace(
                        "_",
                        " ",
                    ).title()

                    st.markdown(
                        f"#### {title}"
                    )

                    if isinstance(value, list):

                        for item in value:

                            st.markdown(
                                f"""
                                <div class="card"
                                     style="margin-bottom:8px;">
                                    {item}
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )

                    else:

                        st.markdown(
                            f"""
                            <div class="card">
                                {value}
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )


    with tabs[6]:

        st.markdown("### Cover letter")

        cover = safe_get(
            data,
            "cover_letter",
            {},
        )

        if cover:

            for key, value in cover.items():

                if value:

                    if key in [
                        "body",
                        "content",
                        "letter",
                    ]:

                        st.text_area(
                            "Generated letter",
                            value=str(value),
                            height=450,
                        )

                    else:

                        st.markdown(
                            f"**{key.replace('_',' ').title()}**"
                        )

                        st.write(value)


    with tabs[7]:

        st.markdown("### Interview preparation")

        interview = safe_get(
            data,
            "interview_questions",
            {},
        )

        if interview:

            for key, value in interview.items():

                if value:

                    st.markdown(
                        f"#### {key.replace('_',' ').title()}"
                    )

                    for item in list_value(value):

                        with st.expander(
                            str(item)[:100]
                        ):
                            st.write(item)


    with tabs[8]:

        st.markdown("### Quality check")

        quality = safe_get(
            data,
            "quality",
            {},
        )

        if quality:

            for key, value in quality.items():

                if value is not None:

                    st.markdown(
                        f"#### {key.replace('_',' ').title()}"
                    )

                    if isinstance(value, list):

                        for item in value:
                            st.write("•", item)

                    else:

                        st.write(value)


    with tabs[9]:

        st.markdown("### Knowledge used")

        sources = safe_get(
            data,
            "rag_sources",
            [],
        )

        guidance = safe_get(
            data,
            "retrieved_guidance",
            [],
        )

        if sources:

            st.markdown(
                """
                <div class="success-box">
                    ✓ Recommendations were informed by the
                    resume-writing knowledge base.
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("#### Sources")

            for source in sources:

                st.markdown(
                    f"""
                    <div class="card"
                         style="margin-bottom:8px;">
                        {source}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        if guidance:

            st.markdown("#### Retrieved guidance")

            for item in guidance:

                with st.expander(
                    str(item)[:80]
                ):

                    st.write(item)


    with tabs[10]:

        st.markdown("### Take your application with you")

        st.markdown(
            """
            <div class="card">
                <div class="card-title">
                    Export your results
                </div>
                <div class="card-subtitle">
                    Download the generated documents for your application.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        def download_export(
            endpoint,
            filename,
            label,
            mime,
        ):

            try:

                response = requests.post(
                    f"{BACKEND_URL}{endpoint}",
                    json=data,
                    timeout=60,
                )

                if response.ok:

                    st.download_button(
                        label,
                        response.content,
                        file_name=filename,
                        mime=mime,
                        use_container_width=True,
                    )

                else:

                    st.error(
                        "Export failed."
                    )

            except Exception as e:

                st.error(str(e))

        with col1:

            download_export(
                "/export/resume",
                "CareerCraft_Tailored_Resume.docx",
                "↓  Download Resume",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )

        with col2:

            download_export(
                "/export/cover-letter",
                "CareerCraft_Cover_Letter.docx",
                "↓  Download Cover Letter",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )

        with col3:

            download_export(
                "/export/report",
                "CareerCraft_Analysis_Report.pdf",
                "↓  Download Report",
                "application/pdf",
            )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "← Analyze another application",
            use_container_width=True,
        ):

            st.session_state.analysis = None
            st.session_state.uploaded_name = None
            st.rerun()


st.markdown(
    """
    <div class="footer">
        CareerCraft AI · Built for smarter job applications
    </div>
    """,
    unsafe_allow_html=True,
)
