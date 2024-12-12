import streamlit as st

st.set_page_config(page_title="anh Nhân đẹp trai", page_icon=":skull:", layout="centered")
st.warning("Cảnh báo! chủ page bị đẹp trai", icon="⚠️")
#setup_session_state_variable
if "l" not in st.session_state:
    st.session_state.l=0
if "f" not in st.session_state:
    st.session_state.f=0
if "pressed" not in st.session_state:
    st.session_state.pressed = False
if "ach" not in st.session_state:
    st.session_state.ach = True
if 'cmm' not in st.session_state:
    st.session_state.cmm = False
#Button
c1, c2 = st.columns(2)
with c1:
    st.image("me.png", width=200)
with c2:
    st.title("sWeater's blog")
    st.write("Yêu lý bí tin:DD")
    
    c21, c22 = st.columns(2)
    with c21:
        T = "Followed" if st.session_state.pressed else "Follow page😍"
        fl = st.button(T)
        if fl:
            st.session_state.pressed = not st.session_state.pressed
            if st.session_state.pressed:
                st.session_state.f+=1
            else:
                st.session_state.f-=1
    with c22:
        like = st.button("Like page")
        if like:
            st.session_state.l+=1
     
c1, c2 = st.columns(2)
with c1:
    st.write("Follower: ",st.session_state.f)
with c2:
    st.write("likes: ",st.session_state.l)
#Button
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("Post"):
        st.session_state.ach = True
with c2:
    bth = st.button("About me")
    if bth:
        st.session_state.ach = False
with c3:
    ifo = st.button("Information")
    if ifo:
        st.session_state.ach = False
with c4:
    img = st.button("Image") 
    if img:
        st.session_state.ach = False

if st.session_state.ach:
    st.header("Post:")
    c1, c2 = st.columns(2)
    with c1:
        st.image("post.png", width=400)
    with c2:
        st.write("10:22 PM - 18/10/2024")
        st.markdown("Deadline 12h đêm nay và tôi chưa biết nên làm gì, nhưng không sao vì tôi là một sinh viên thư giãn=)")
        st.session_state.cmm = st.button("Add comment")
        if st.session_state.cmm:
            w_cmm = st.text_area("Write your comment:")
if bth:
    st.header("About me:")
    st.write("I'm just a chill guy:D")
    st.image("chillguy.jpg", width=600)
if ifo:
    st.header("Information:")
    st.write("🌏 Sống tại: Kon Tum, Viet Nam")
    st.write("🎓 Học vấn: Học tại trường THPT Chuyên NTT Kon Tum")
    st.write("🏢 Công việc: Làm việc tại CKTU-CKT Union")
    st.write("📆 Ngày sinh: 01/01/2009")
if img:
    st.header("Image:")
    st.warning("No image found!", icon="😭")
with st.sidebar:
    st.markdown("Nhân SEGMA fact summary!")
    st.image("deptrai.jpg", width=600)
