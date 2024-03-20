import streamlit as st


st.set_page_config(
    page_title="인터넷 사진, 영상들",
    page_icon="images/monsterball.png",
)

st.markdown("""
<style>
img {
	max-height: 300px;
}
.streamlit-expanderContent div {
    display: flex;
    justify-content: center;
    font-size: 20px;
}
[data-testid="stExpanderToggleIcon"] {
    visibility: hidden;
}
.streamlit-expanderHeader {
    pointer-events: none;
}
[data-testid="StyledFullScreenButton"] {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


st.image("images/default.png",
         width=50)
st.title("streamlit 이미지 저장소")
st.markdown("**이미지**을 하나씩 추가해서 도감을 채워보세요!")


type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "러다이트 운동",
        "types": ["물", "비행"],
        "image_url": "https://i.namu.wiki/i/XuDe2WGyVZYqjy1aqIGYjSoLm2L1a1M-nvhBN1YaAKIQ_oA-k-jGnY9DMWDgWjaGbtLKZsjKQhmjwYUNnTymPx3qVOc9IQ2eCmtsVigHUo0Arl0VIdp_hma-VCUk4f2QK-TC8fNWPCximOKDDl5oYg.webp",
    },
    {
        "name": "메이플자이",
        "types": ["물", "악"],
        "image_url": "https://i.namu.wiki/i/YzFysjx3NdoZEgJURxDhnJjygzk2vUh8ebQIjBYpOSxQRff19LlBT2PrzUZvrfXu3dhE3Rw-ioatfnt1kmDp1SUKTF_LpxNnsaMrwUiuZHGyzU08Fs_WzoVIAneJF1WTAH-miSAZAOv_aDLspPHP_g.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
]

if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons


example_image = {
    "name": "알로라 디그다",
    "types": ["땅", "강철"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/alora_digda.webp"
}

auto_complete = st.toggle("예시 데이터로 채우기")
with st.form("form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="이미지 이름",
            value=example_image["name"] if auto_complete else ""
        )
    with col2:
        types = st.multiselect(
            label="이미지 속성",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_image["types"] if auto_complete else []
        )
    
    image_url = st.text_input(
        label="이미지 URL",
        value=example_image["image_url"] if auto_complete else ""
    )
    submit = st.form_submit_button(label="submit")
    if submit:
        if not name:
            st.error("이미지의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("이미지의 속성을 적어도 한개 선택해주세요.")
        else:
            st.success("이미지를 추가할 수 있습니다.")
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/default.png"
            })
video_link = [
   "https://cdn.openai.com/sora/videos/ships-in-coffee.mp4",
   "https://cdn.openai.com/sora/videos/backward-jogger.mp4",
   "https://cdn.openai.com/sora/videos/zen-garden-gnome.mp4"
]

# session_state에 비디오 링크 리스트를 초기화합니다.
if 'video_links' not in st.session_state:
    st.session_state.video_links = []


with st.form("video_form"):
    # 사용자로부터 비디오 링크를 입력받습니다.
    new_video_link = st.text_input("비디오 링크를 입력하세요:")
    # "링크 추가" 버튼을 생성하고, 클릭 시 동작을 정의합니다.
    if st.form_submit_button(label="submit"):
        if new_video_link:
            # 입력된 링크를 session_state의 리스트에 추가합니다.
            st.session_state.video_links.append(new_video_link)
            # 입력 필드를 초기화합니다.
            st.experimental_rerun()
        else:
            st.error("비디오 링크를 입력해주세요.")

# 비디오 링크의 개수에 따라 필요한 행의 수를 계산
# 한 행에 2개의 비디오를 배치하므로, 전체 길이를 2로 나눈 후 올림
num_rows = -(-len(video_link) // 2)  # 올림 처리를 위한 방법

for i in range(num_rows):
    cols = st.columns(2)  # 2개의 컬럼 생성
    for j in range(2):  # 각 행에 2개의 컬럼이 있으므로, 2번 반복
        index = i*2 + j  # 현재 비디오의 인덱스 계산
        if index < len(video_link):  # 인덱스가 비디오 링크 리스트의 범위 내인지 확인
            with cols[j]:  # 해당 컬럼 선택
                st.video(video_link[index])  # 비디오 표시
                
for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon['name']}**", expanded=True):
                st.image(pokemon["image_url"],use_column_width=True)
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text(" / ".join(emoji_types))
                sub_col1,sub_col2 = st.columns(2)
                with sub_col1:
                    delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                    if delete_button:
                        del st.session_state.pokemons[i+j]
                        st.rerun()
                with sub_col2:
                    download_button = st.download_button("다운로드",data=pokemon["image_url"],key=f"download_{i,j}")
