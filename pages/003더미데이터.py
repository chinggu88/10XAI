import requests
import streamlit as st
import pandas as pd
import numpy as np
import time

# st.write("DB username:", st.secrets["OPENAI_API_KEY"])
# gitst.write("DB password:", st.secrets["MYSQL_URL"])

grid = st.columns(5)
with grid[0]:
    st.write('title > 음식점 이름')
with grid[1]:
    st.write('score > 음식점 평점')
with grid[2]:
    st.write('region > 위치')
with grid[3]:
    st.write('url > 정보 링크')
with grid[4]:
    st.write('statu > 오픈여부')



[
	{
		"idx" : 1,
		"title" : "오한수우육면가",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/FAI1kwcx2xBw",
		"status" : 1
	},
	{
		"idx" : 2,
		"title" : "파낙스",
		"score" : "3.8",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/t-t8wkagjn",
		"status" : 1
	},
	{
		"idx" : 3,
		"title" : "효뜨",
		"score" : "3.8",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/Woc7YBYziVyW",
		"status" : 1
	},
	{
		"idx" : 4,
		"title" : "콘디토리 오븐",
		"score" : "3.8",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/8tOY4jZRGXtO",
		"status" : 1
	},
	{
		"idx" : 5,
		"title" : "카페노티드",
		"score" : "3.8",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/jkx7N9nC51cb",
		"status" : 1
	},
	{
		"idx" : 6,
		"title" : "크리스피프레시",
		"score" : "3.8",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/sAzQ0XVEAG7Q",
		"status" : 1
	},
	{
		"idx" : 7,
		"title" : "미켈레 커피",
		"score" : "3.8",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/5-UVYbMfLmM_",
		"status" : 1
	},
	{
		"idx" : 8,
		"title" : "신동양반점",
		"score" : "3.8",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/aUJGmPSsqi",
		"status" : 1
	},
	{
		"idx" : 9,
		"title" : "서울로인",
		"score" : "3.8",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/6vMjHiGSxd7l",
		"status" : 1
	},
	{
		"idx" : 10,
		"title" : "여의도따로국밥",
		"score" : "3.8",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/8ADz0USfBu",
		"status" : 1
	},
	{
		"idx" : 11,
		"title" : "폴트버거",
		"score" : "3.8",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/-ofoysnqyN4G",
		"status" : 1
	},
	{
		"idx" : 12,
		"title" : "화해당",
		"score" : "3.8",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/GQ9rFNF45M",
		"status" : 1
	},
	{
		"idx" : 13,
		"title" : "랑만",
		"score" : "3.8",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/9uSFVuqjiKQy",
		"status" : 1
	},
	{
		"idx" : 14,
		"title" : "피그인더가든",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/6NCfdsUYQspc",
		"status" : 1
	},
	{
		"idx" : 15,
		"title" : "리스토란테에오",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/u51i7rdoVc",
		"status" : 1
	},
	{
		"idx" : 16,
		"title" : "워킹온더클라우드",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/wi6UYfVcvB",
		"status" : 1
	},
	{
		"idx" : 17,
		"title" : "야마야",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/tEaW9Sv5So",
		"status" : 1
	},
	{
		"idx" : 18,
		"title" : "63뷔페 파빌리온",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/b6GHM15NoG",
		"status" : 1
	},
	{
		"idx" : 19,
		"title" : "창고43",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/ZCOtYtuxn7",
		"status" : 1
	},
	{
		"idx" : 20,
		"title" : "경천애인2237",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/lrLUXB1zGPSk",
		"status" : 1
	},
	{
		"idx" : 21,
		"title" : "폴앤폴리나",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/Slk_zHAHgi",
		"status" : 1
	},
	{
		"idx" : 22,
		"title" : "슈치쿠",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/iJB9eZaJbc",
		"status" : 1
	},
	{
		"idx" : 23,
		"title" : "브로트아트",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/F8OblgQYNutM",
		"status" : 1
	},
	{
		"idx" : 24,
		"title" : "화목순대국",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/w61QdM8E4V",
		"status" : 1
	},
	{
		"idx" : 25,
		"title" : "대원",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/VwoitMFQIz",
		"status" : 1
	},
	{
		"idx" : 26,
		"title" : "영원식당",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/w7cbYC9HSX",
		"status" : 1
	},
	{
		"idx" : 27,
		"title" : "스펙트럼",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/9BVyOMgGS3KX",
		"status" : 1
	},
	{
		"idx" : 28,
		"title" : "와인웍스",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/j7ORWvwwsj6O",
		"status" : 1
	},
	{
		"idx" : 29,
		"title" : "우아",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/Vu2E2Y4ukPd9",
		"status" : 1
	},
	{
		"idx" : 30,
		"title" : "콘부",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/zzESb_vs8Fe8",
		"status" : 1
	},
	{
		"idx" : 31,
		"title" : "순옥이네 명가",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/jdWf9RNX-rq7",
		"status" : 1
	},
	{
		"idx" : 32,
		"title" : "리치몬드",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/3E16BiCYYIQN",
		"status" : 1
	},
	{
		"idx" : 33,
		"title" : "이여곰탕",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/uenSxqqx54s1",
		"status" : 1
	},
	{
		"idx" : 34,
		"title" : "호우섬",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/2QpKyRsMPXeh",
		"status" : 1
	},
	{
		"idx" : 35,
		"title" : "백리향",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/eI6hbHYX75",
		"status" : 1
	},
	{
		"idx" : 36,
		"title" : "아트리오",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/012Bpc16Zc",
		"status" : 1
	},
	{
		"idx" : 37,
		"title" : "스시미소",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/F-n-qxLzWx-t",
		"status" : 1
	},
	{
		"idx" : 38,
		"title" : "그리츠",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/k7xtPHkds1",
		"status" : 1
	},
	{
		"idx" : 39,
		"title" : "진가와",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/HIMq37ykIyxq",
		"status" : 1
	},
	{
		"idx" : 40,
		"title" : "번패티번",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/WUdTrEptWo7L",
		"status" : 1
	},
	{
		"idx" : 41,
		"title" : "아루히 니와",
		"score" : "4.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/wbDJ-JHE4yqo",
		"status" : 1
	},
	{
		"idx" : 42,
		"title" : "스시다정",
		"score" : "4.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/_ohhmMS6_UR_",
		"status" : 1
	},
	{
		"idx" : 43,
		"title" : "바이러닉에스프레소바",
		"score" : "4.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/DgRCxk7eoWVA",
		"status" : 1
	},
	{
		"idx" : 44,
		"title" : "스시아라타",
		"score" : "4.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/vZ74ooBDahfg",
		"status" : 1
	},
	{
		"idx" : 45,
		"title" : "로바",
		"score" : "4.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/oK1UfMipJZ3Q",
		"status" : 1
	},
	{
		"idx" : 46,
		"title" : "테일러 커피",
		"score" : "4.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/ulZ1u8vYwjgF",
		"status" : 1
	},
	{
		"idx" : 47,
		"title" : "정인면옥",
		"score" : "4.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/extAj1Oeyx",
		"status" : 1
	},
	{
		"idx" : 48,
		"title" : "아루히",
		"score" : "4.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/SKXF6cbFWcCl",
		"status" : 1
	},
	{
		"idx" : 49,
		"title" : "가양칼국수버섯매운탕",
		"score" : "4.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/jOf_M6zFb2",
		"status" : 1
	},
	{
		"idx" : 50,
		"title" : "르프리크",
		"score" : "4.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/qT81KJGY_xXy",
		"status" : 1
	},
	{
		"idx" : 51,
		"title" : "브루클린더버거조인트",
		"score" : "4.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/uUHoZ6D0slBh",
		"status" : 1
	},
	{
		"idx" : 52,
		"title" : "갓포아키",
		"score" : "4.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/b1xCK6SHxpcP",
		"status" : 1
	},
	{
		"idx" : 53,
		"title" : "모던샤브하우스",
		"score" : "4.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/yJ5NWLqq5Hwh",
		"status" : 1
	},
	{
		"idx" : 54,
		"title" : "목탄장",
		"score" : "4.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/GfUIZMDH-baA",
		"status" : 1
	},
	{
		"idx" : 55,
		"title" : "허리헝그리",
		"score" : "4.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/1ubJn78JKcyx",
		"status" : 1
	},
	{
		"idx" : 56,
		"title" : "오복수산",
		"score" : "4.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/MuP_lze1DtYJ",
		"status" : 1
	},
	{
		"idx" : 57,
		"title" : "렌위치",
		"score" : "4.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/L6yxPDbyDGBC",
		"status" : 1
	},
	{
		"idx" : 58,
		"title" : "도원스타일",
		"score" : "4.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/j8VYns4cRJGn",
		"status" : 1
	},
	{
		"idx" : 59,
		"title" : "진주집",
		"score" : "4.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/XY-zb7lkI_",
		"status" : 1
	},
	{
		"idx" : 60,
		"title" : "하쯔호",
		"score" : "4.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/T9ADrw4L6X",
		"status" : 1
	},
	{
		"idx" : 61,
		"title" : "아이엠베이글",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/ao_mvjfro_uY",
		"status" : 1
	},
	{
		"idx" : 62,
		"title" : "그레이에스프레소",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/kcl5lSQnMVtw",
		"status" : 1
	},
	{
		"idx" : 63,
		"title" : "카멜 커피",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/EjvU1nvQ_dh-",
		"status" : 1
	},
	{
		"idx" : 64,
		"title" : "더스테이크하우스",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/6TlXE64cA0",
		"status" : 1
	},
	{
		"idx" : 65,
		"title" : "나폴레옹제과점",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/RPCbdKbFnYMn",
		"status" : 1
	},
	{
		"idx" : 66,
		"title" : "슈퍼말차",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/x9cRmP8MGFtz",
		"status" : 1
	},
	{
		"idx" : 67,
		"title" : "시마스시",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/27f15PKXH6Dm",
		"status" : 1
	},
	{
		"idx" : 68,
		"title" : "모던눌랑",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/yqz5jH7unQ8H",
		"status" : 1
	},
	{
		"idx" : 69,
		"title" : "훠궈야",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/PuZ7ijpWAW1f",
		"status" : 1
	},
	{
		"idx" : 70,
		"title" : "에덴식당",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/KK-pwEo9cWnJ",
		"status" : 1
	},
	{
		"idx" : 71,
		"title" : "카페마마스",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/UOB79rPLiLv4",
		"status" : 1
	},
	{
		"idx" : 72,
		"title" : "점보씨푸드",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/NpcPty3ov4fW",
		"status" : 1
	},
	{
		"idx" : 73,
		"title" : "카페꼼마&얀 쿠브레",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/dAgT-cAaM_M3",
		"status" : 1
	},
	{
		"idx" : 74,
		"title" : "비엣남",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/nAgyMXEpZMUd",
		"status" : 1
	},
	{
		"idx" : 75,
		"title" : "올댓커피",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/YxzpedSG1dkJ",
		"status" : 1
	},
	{
		"idx" : 76,
		"title" : "진진만두국",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/MUBVC_eFwV",
		"status" : 1
	},
	{
		"idx" : 77,
		"title" : "패트릭스와플",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/IdAtdbNb07",
		"status" : 1
	},
	{
		"idx" : 78,
		"title" : "오늘은즉떡",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/ZMOHReVMl3au",
		"status" : 1
	},
	{
		"idx" : 79,
		"title" : "카페꼼마",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/YFVL9DmlYo1h",
		"status" : 1
	},
	{
		"idx" : 80,
		"title" : "신원",
		"score" : "3.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/onisMiN0SQ",
		"status" : 1
	},
	{
		"idx" : 81,
		"title" : "더아트리움라운지",
		"score" : "4.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/fjpt9WoQzG1m",
		"status" : 1
	},
	{
		"idx" : 82,
		"title" : "히노노리",
		"score" : "4.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/vVNatXWeueiC",
		"status" : 1
	},
	{
		"idx" : 83,
		"title" : "오복수산참치",
		"score" : "4.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/HQ-73o45zp2m",
		"status" : 1
	},
	{
		"idx" : 84,
		"title" : "어만두",
		"score" : "4.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/GAiBBgjLfFhX",
		"status" : 1
	},
	{
		"idx" : 85,
		"title" : "고방채",
		"score" : "4.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/tlJp7CDYMSbr",
		"status" : 1
	},
	{
		"idx" : 86,
		"title" : "별미볶음점",
		"score" : "4.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/9dwjvKWC-R",
		"status" : 1
	},
	{
		"idx" : 87,
		"title" : "세상의모든아침",
		"score" : "4.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/HIxhmGe7yX1A",
		"status" : 1
	},
	{
		"idx" : 88,
		"title" : "스시온정",
		"score" : "4.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/TDnb8_8edF1Q",
		"status" : 1
	},
	{
		"idx" : 89,
		"title" : "더플레이트디저트",
		"score" : "4.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/YZwtMuppX8x9",
		"status" : 1
	},
	{
		"idx" : 90,
		"title" : "바스버거",
		"score" : "4.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/XM7xxjNeWPIL",
		"status" : 1
	},
	{
		"idx" : 91,
		"title" : "타마스시",
		"score" : "4.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/U-kUakm3O2",
		"status" : 1
	},
	{
		"idx" : 92,
		"title" : "카페 레이어드",
		"score" : "4.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/aTEl_UE0jW2u",
		"status" : 1
	},
	{
		"idx" : 93,
		"title" : "라케이브",
		"score" : "4.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/Yu1ogHAITWLV",
		"status" : 1
	},
	{
		"idx" : 94,
		"title" : "잠수교집",
		"score" : "4.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/FyK6YtTz0jWN",
		"status" : 1
	},
	{
		"idx" : 95,
		"title" : "잇샐러드",
		"score" : "4.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/F6f-p04-Ku8n",
		"status" : 1
	},
	{
		"idx" : 96,
		"title" : "버거플리즈",
		"score" : "4.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/VoNLBfMiLP1x",
		"status" : 1
	},
	{
		"idx" : 97,
		"title" : "브로드웨이",
		"score" : "4.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/fP8F84CZp9",
		"status" : 1
	},
	{
		"idx" : 98,
		"title" : "더미",
		"score" : "4.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/9p2UmZTnWq6I",
		"status" : 1
	},
	{
		"idx" : 99,
		"title" : "테이스팅룸",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/_o3olGVbwpjc",
		"status" : 1
	},
	{
		"idx" : 100,
		"title" : "마리포사",
		"score" : "4.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/hsq0rSuOeCnW",
		"status" : 1
	},
	{
		"idx" : 101,
		"title" : "마얘",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/OM0hR6_fz-CB",
		"status" : 1
	},
	{
		"idx" : 102,
		"title" : "라공방",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/CEM1f22chF0F",
		"status" : 1
	},
	{
		"idx" : 103,
		"title" : "제스트",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/T8PmfPGsk7",
		"status" : 1
	},
	{
		"idx" : 104,
		"title" : "온더보더",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/cvTQzvV5Rh",
		"status" : 1
	},
	{
		"idx" : 105,
		"title" : "수티",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/zSKUwULuvw2y",
		"status" : 1
	},
	{
		"idx" : 106,
		"title" : "올라6",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/_fViqIEBSP",
		"status" : 1
	},
	{
		"idx" : 107,
		"title" : "판다익스프레스",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/K-iiCTw_EngC",
		"status" : 1
	},
	{
		"idx" : 108,
		"title" : "소호정",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/1A7FjBO6DP",
		"status" : 1
	},
	{
		"idx" : 109,
		"title" : "이와타",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/-5Iy4aOQS9qd",
		"status" : 1
	},
	{
		"idx" : 110,
		"title" : "퍼스트플러스에이드",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/Kejb-ozWBmtX",
		"status" : 1
	},
	{
		"idx" : 111,
		"title" : "다미",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/0U05gCvwoB",
		"status" : 1
	},
	{
		"idx" : 112,
		"title" : "커피기업",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/0Qtw95mr5rtE",
		"status" : 1
	},
	{
		"idx" : 113,
		"title" : "유방녕",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/holb3kQZArHu",
		"status" : 1
	},
	{
		"idx" : 114,
		"title" : "브레드피트",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/4CZSAPjFa_",
		"status" : 1
	},
	{
		"idx" : 115,
		"title" : "카레오",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/ER5EHAUDBL_m",
		"status" : 1
	},
	{
		"idx" : 116,
		"title" : "차알",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/71RifRZ3zVwn",
		"status" : 1
	},
	{
		"idx" : 117,
		"title" : "와인주막차차",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/1apBSMp071gr",
		"status" : 1
	},
	{
		"idx" : 118,
		"title" : "강가",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/Mr6REcI-FJ",
		"status" : 1
	},
	{
		"idx" : 119,
		"title" : "더누들바",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/nHnlx2cT9ZYG",
		"status" : 1
	},
	{
		"idx" : 120,
		"title" : "여의도황소곱창",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/RNelVugQ6jaC",
		"status" : 1
	},
	{
		"idx" : 121,
		"title" : "쿠치나후",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/GQjsxSZyiA",
		"status" : 1
	},
	{
		"idx" : 122,
		"title" : "제이레스토랑",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/qzTcr9i7zKji",
		"status" : 1
	},
	{
		"idx" : 123,
		"title" : "서궁",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/XuZZidvThL",
		"status" : 1
	},
	{
		"idx" : 124,
		"title" : "VVERTIGO",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/936pLbBVTvx-",
		"status" : 1
	},
	{
		"idx" : 125,
		"title" : "마호가니커피",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/LgShfnYRjzUT",
		"status" : 1
	},
	{
		"idx" : 126,
		"title" : "모도우",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/4QJYPino5gOx",
		"status" : 1
	},
	{
		"idx" : 127,
		"title" : "10g",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/PYfIE3IWQwn4",
		"status" : 1
	},
	{
		"idx" : 128,
		"title" : "청수",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/bKmTaXaGBR",
		"status" : 1
	},
	{
		"idx" : 129,
		"title" : "삼씨오화",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/wPDlDF0RNpd2",
		"status" : 1
	},
	{
		"idx" : 130,
		"title" : "진진만두국",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/9LTHjM6Bwa",
		"status" : 1
	},
	{
		"idx" : 131,
		"title" : "제이렘333",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/DyROx2uVeG",
		"status" : 1
	},
	{
		"idx" : 132,
		"title" : "홍설",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/PiY3BFDnIl",
		"status" : 1
	},
	{
		"idx" : 133,
		"title" : "희정식당",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/YlgWi3gLVt",
		"status" : 1
	},
	{
		"idx" : 134,
		"title" : "을지다락",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/P6sxWy8cP1Q1",
		"status" : 1
	},
	{
		"idx" : 135,
		"title" : "탭퍼블릭",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/SKSIvjIVqNL8",
		"status" : 1
	},
	{
		"idx" : 136,
		"title" : "후라토식당",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/0zsXW2P96_Io",
		"status" : 1
	},
	{
		"idx" : 137,
		"title" : "하동관",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/iJGPnHNEF2",
		"status" : 1
	},
	{
		"idx" : 138,
		"title" : "고메브레드",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/-OgBMKE48J",
		"status" : 1
	},
	{
		"idx" : 139,
		"title" : "용호낙지",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/cC196LzyUrUX",
		"status" : 1
	},
	{
		"idx" : 140,
		"title" : "남기분면",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/fMMEPBzA7h9d",
		"status" : 1
	},
	{
		"idx" : 141,
		"title" : "리샨",
		"score" : "3.5",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/yPGoPZ8niU",
		"status" : 1
	},
	{
		"idx" : 142,
		"title" : "SMT 라운지",
		"score" : "3.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/WQC2WEzHorFb",
		"status" : 1
	},
	{
		"idx" : 143,
		"title" : "카페마마스",
		"score" : "3.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/M_gj0BVmc_",
		"status" : 1
	},
	{
		"idx" : 144,
		"title" : "더플레이스",
		"score" : "3.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/g5B_SLQOZ-5x",
		"status" : 1
	},
	{
		"idx" : 145,
		"title" : "블루보틀",
		"score" : "3.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/JpgnqGWT_C09",
		"status" : 1
	},
	{
		"idx" : 146,
		"title" : "베즐리",
		"score" : "3.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/rPVvvBblERyO",
		"status" : 1
	},
	{
		"idx" : 147,
		"title" : "대동문",
		"score" : "3.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/I-FGn5cOGk",
		"status" : 1
	},
	{
		"idx" : 148,
		"title" : "수하동",
		"score" : "3.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/cKoxx-R3-IRL",
		"status" : 1
	},
	{
		"idx" : 149,
		"title" : "흑돈가",
		"score" : "3.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/BpZTW8_-Gr",
		"status" : 1
	},
	{
		"idx" : 150,
		"title" : "하카타분코 오토코쥬쿠",
		"score" : "3.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/_7Wc99BiEbBt",
		"status" : 1
	},
	{
		"idx" : 151,
		"title" : "아티제",
		"score" : "3.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/pzUVwNZRHj",
		"status" : 1
	},
	{
		"idx" : 152,
		"title" : "버틀러 커피",
		"score" : "3.4",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/5xJ0fs66AcJv",
		"status" : 1
	},
	{
		"idx" : 153,
		"title" : "쓰리버즈",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/UHTJgl0hjqem",
		"status" : 1
	},
	{
		"idx" : 154,
		"title" : "제일제면소",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/VrEHR4ri04",
		"status" : 1
	},
	{
		"idx" : 155,
		"title" : "올라",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/RncaLFBVKZ",
		"status" : 1
	},
	{
		"idx" : 156,
		"title" : "사대부집곳간",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/t7IULT5LwAXc",
		"status" : 1
	},
	{
		"idx" : 157,
		"title" : "에그슬럿",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/oJuGDRVqk6fp",
		"status" : 1
	},
	{
		"idx" : 158,
		"title" : "아비꼬",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/wqdiz7vEqW",
		"status" : 1
	},
	{
		"idx" : 159,
		"title" : "동해도",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/Y8U4u99a_7",
		"status" : 1
	},
	{
		"idx" : 160,
		"title" : "그리디몬",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/HwTSXJ1Fc1sM",
		"status" : 1
	},
	{
		"idx" : 161,
		"title" : "남대문커피",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/P39PHC29eF_E",
		"status" : 1
	},
	{
		"idx" : 162,
		"title" : "도깨비굴",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/9W827NkHoN2G",
		"status" : 1
	},
	{
		"idx" : 163,
		"title" : "마마된장",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/J33HE84Xyzo2",
		"status" : 1
	},
	{
		"idx" : 164,
		"title" : "플리퍼스스탠드",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/9kFaKa3cHp-p",
		"status" : 1
	},
	{
		"idx" : 165,
		"title" : "사리원불고기",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/MMHlPSKCGX",
		"status" : 1
	},
	{
		"idx" : 166,
		"title" : "송옥",
		"score" : "3.3",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/Jrf8lSnyuH52",
		"status" : 1
	},
	{
		"idx" : 167,
		"title" : "도쿄등심",
		"score" : "3.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/BpfQcMHlNzuf",
		"status" : 1
	},
	{
		"idx" : 168,
		"title" : "콘타이",
		"score" : "3.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/on4HjCQUkrp4",
		"status" : 1
	},
	{
		"idx" : 169,
		"title" : "이탈리",
		"score" : "3.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/TR4e5vYD2II3",
		"status" : 1
	},
	{
		"idx" : 170,
		"title" : "이도맨숀",
		"score" : "3.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/f9UYnjDJmxuV",
		"status" : 1
	},
	{
		"idx" : 171,
		"title" : "생어거스틴",
		"score" : "3.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/Lh9Vu2ITkR",
		"status" : 1
	},
	{
		"idx" : 172,
		"title" : "플러피",
		"score" : "3.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/r_d0e4cxwXeQ",
		"status" : 1
	},
	{
		"idx" : 173,
		"title" : "농민백암왕순대",
		"score" : "3.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/hoo3ljEjnU",
		"status" : 1
	},
	{
		"idx" : 174,
		"title" : "미도인",
		"score" : "3.2",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/RekQYOH6DJx-",
		"status" : 1
	},
	{
		"idx" : 175,
		"title" : "알로하포케",
		"score" : "3.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/543rR3d6jdku",
		"status" : 1
	},
	{
		"idx" : 176,
		"title" : "오미식당",
		"score" : "3.1",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/r-Ysw_NyrLju",
		"status" : 1
	},
	{
		"idx" : 177,
		"title" : "버거헌터",
		"score" : "3.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/0URKEqtYST",
		"status" : 1
	},
	{
		"idx" : 178,
		"title" : "홍수계찜닭",
		"score" : "3.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/t_z2hofGqtsT",
		"status" : 1
	},
	{
		"idx" : 179,
		"title" : "평화다방",
		"score" : "3.0",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/OJi_escSLd1k",
		"status" : 1
	},
	{
		"idx" : 180,
		"title" : "엘리스파이",
		"score" : "2.9",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/Ul8cDPrW6x",
		"status" : 1
	},
	{
		"idx" : 181,
		"title" : "로라스 블랑",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/-W1K_6yVe819",
		"status" : 1
	},
	{
		"idx" : 182,
		"title" : "뉴오리진",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/erVi_8OIr7ZI",
		"status" : 1
	},
	{
		"idx" : 183,
		"title" : "구이구이",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/bPeUm80KJf",
		"status" : 1
	},
	{
		"idx" : 184,
		"title" : "배꼽집",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/prRM_-LJVt9z",
		"status" : 1
	},
	{
		"idx" : 185,
		"title" : "마츠노하나",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/-4EQwN3HjMqW",
		"status" : 1
	},
	{
		"idx" : 186,
		"title" : "고봉삼계탕",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/hs2ANEwQoV",
		"status" : 1
	},
	{
		"idx" : 187,
		"title" : "정육면체",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/3BQluu3rZmWG",
		"status" : 1
	},
	{
		"idx" : 188,
		"title" : "차이나플레인",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/iwNzDJtyJdTL",
		"status" : 1
	},
	{
		"idx" : 189,
		"title" : "사위식당",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/hYxmhafYoGLK",
		"status" : 1
	},
	{
		"idx" : 190,
		"title" : "탐광",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/clJJbi_DtH22",
		"status" : 1
	},
	{
		"idx" : 191,
		"title" : "아그라",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/R4ZddOW6VYr8",
		"status" : 1
	},
	{
		"idx" : 192,
		"title" : "패트릭스와플",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/qVw_xjHsqG",
		"status" : 1
	},
	{
		"idx" : 193,
		"title" : "그리너리샐러드",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/1OuW5Oxntk",
		"status" : 1
	},
	{
		"idx" : 194,
		"title" : "삼육공",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/IJSPxjCIRBTi",
		"status" : 1
	},
	{
		"idx" : 195,
		"title" : "삼성혈 해물탕",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/Sx4rB8U5U0CE",
		"status" : 1
	},
	{
		"idx" : 196,
		"title" : "나이스웨더",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/XlWRi2MQjhWV",
		"status" : 1
	},
	{
		"idx" : 197,
		"title" : "긴자 바이린",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/xpcrab06eLOA",
		"status" : 1
	},
	{
		"idx" : 198,
		"title" : "몽이닭발",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/OcbIt3Ag1RBh",
		"status" : 1
	},
	{
		"idx" : 199,
		"title" : "돈까스1985",
		"score" : "3.7",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/RBiGzEcTysE_",
		"status" : 1
	},
	{
		"idx" : 200,
		"title" : "37그릴앤바",
		"score" : "3.6",
		"region" : "여의도",
		"url" : "https://www.mangoplate.com/restaurants/UMNClCWWJo",
		"status" : 1
	},
	{
		"idx" : 201,
		"title" : "비야게레로",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/fPi6OZ3r-u",
		"status" : 1
	},
	{
		"idx" : 202,
		"title" : "파씨오네",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/mfwd78vEtS",
		"status" : 1
	},
	{
		"idx" : 203,
		"title" : "꼼다비뛰드",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/DM2xUaLRreaa",
		"status" : 1
	},
	{
		"idx" : 204,
		"title" : "지아니스나폴리",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/6M3GR-y14f",
		"status" : 1
	},
	{
		"idx" : 205,
		"title" : "골드피쉬딤섬퀴진",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/PalvouUA1j",
		"status" : 1
	},
	{
		"idx" : 206,
		"title" : "정돈 프리미엄",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/MyeCz_JlSgan",
		"status" : 1
	},
	{
		"idx" : 207,
		"title" : "중앙해장",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/phK__CKmeq-X",
		"status" : 1
	},
	{
		"idx" : 208,
		"title" : "봉밀가",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/kkTSEK1nWp",
		"status" : 1
	},
	{
		"idx" : 209,
		"title" : "밍글스",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/YM03z4lpvY",
		"status" : 1
	},
	{
		"idx" : 210,
		"title" : "콴안다오",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/2_sFMbsZC9HC",
		"status" : 1
	},
	{
		"idx" : 211,
		"title" : "길버트버거앤프라이즈",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/W7ie2Qm0gZ",
		"status" : 1
	},
	{
		"idx" : 212,
		"title" : "경천애인 2237",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/mcv53uaozM",
		"status" : 1
	},
	{
		"idx" : 213,
		"title" : "갓포아키",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/Qmjyzoyz2-",
		"status" : 1
	},
	{
		"idx" : 214,
		"title" : "136길육미",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/DtNd7lLzTLZU",
		"status" : 1
	},
	{
		"idx" : 215,
		"title" : "육전식당",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/z-4tCw3TKCKn",
		"status" : 1
	},
	{
		"idx" : 216,
		"title" : "권숙수",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/U1VsV7e2K2",
		"status" : 1
	},
	{
		"idx" : 217,
		"title" : "새들러하우스",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/_lwTLhPuzfky",
		"status" : 1
	},
	{
		"idx" : 218,
		"title" : "바게트K",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/UFeL9KXKwjEs",
		"status" : 1
	},
	{
		"idx" : 219,
		"title" : "농민백암순대",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/Ll-IdIOuVv",
		"status" : 1
	},
	{
		"idx" : 220,
		"title" : "대우부대찌개",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/_vXifqRyzj",
		"status" : 1
	},
	{
		"idx" : 221,
		"title" : "카츠8",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/H1BB9ppd0Sbu",
		"status" : 1
	},
	{
		"idx" : 222,
		"title" : "BISTROT de YOUNTVILLE",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/koJ-1vE9dB",
		"status" : 1
	},
	{
		"idx" : 223,
		"title" : "톡톡",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/MIGi8MXfr_",
		"status" : 1
	},
	{
		"idx" : 224,
		"title" : "스시코우지",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/btY7z88DBf",
		"status" : 1
	},
	{
		"idx" : 225,
		"title" : "길목",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/Xg0LDOaBhaPX",
		"status" : 1
	},
	{
		"idx" : 226,
		"title" : "이치에",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/BJk2Z6emjA",
		"status" : 1
	},
	{
		"idx" : 227,
		"title" : "로바타탄요",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/AIodGGqVRYId",
		"status" : 1
	},
	{
		"idx" : 228,
		"title" : "와라야키 쿠이신보",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/jiQPoOdNDqQc",
		"status" : 1
	},
	{
		"idx" : 229,
		"title" : "스시키",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/ugq5zpw24LjX",
		"status" : 1
	},
	{
		"idx" : 230,
		"title" : "젠제로",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/2Tp-I0qkXYwS",
		"status" : 1
	},
	{
		"idx" : 231,
		"title" : "칙피스",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/wvZeJsW78zwk",
		"status" : 1
	},
	{
		"idx" : 232,
		"title" : "페어링룸",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/L_01tNvT5H-Y",
		"status" : 1
	},
	{
		"idx" : 233,
		"title" : "허머스키친",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/RNdc2ShnTc4A",
		"status" : 1
	},
	{
		"idx" : 234,
		"title" : "코슌",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/HmA2OLXpsoT_",
		"status" : 1
	},
	{
		"idx" : 235,
		"title" : "매덕스피자",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/dbZtB1usggE2",
		"status" : 1
	},
	{
		"idx" : 236,
		"title" : "스미카",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/S9i9R3cpZv8Y",
		"status" : 1
	},
	{
		"idx" : 237,
		"title" : "스시인",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/2qaxcbiKhy1A",
		"status" : 1
	},
	{
		"idx" : 238,
		"title" : "고갯마루집",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/jvn2aG4heS",
		"status" : 1
	},
	{
		"idx" : 239,
		"title" : "흐비지떼",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/xLGs-ZuMasCv",
		"status" : 1
	},
	{
		"idx" : 240,
		"title" : "르뱅룰즈",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/Ev9M9HBwCqO9",
		"status" : 1
	},
	{
		"idx" : 241,
		"title" : "미라이",
		"score" : "4.8",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/iMRRP69qtkeO",
		"status" : 1
	},
	{
		"idx" : 242,
		"title" : "시라카와",
		"score" : "4.8",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/9EVyzauilukl",
		"status" : 1
	},
	{
		"idx" : 243,
		"title" : "페리지",
		"score" : "4.8",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/pI112Z4JVmBn",
		"status" : 1
	},
	{
		"idx" : 244,
		"title" : "명랑회관",
		"score" : "4.8",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/vAGwdLA9j1IM",
		"status" : 1
	},
	{
		"idx" : 245,
		"title" : "상진식감",
		"score" : "4.8",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/2L8yQMWy1Eye",
		"status" : 1
	},
	{
		"idx" : 246,
		"title" : "스시카나에",
		"score" : "4.7",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/UjiK7BUxljkP",
		"status" : 1
	},
	{
		"idx" : 247,
		"title" : "패티앤베지스",
		"score" : "4.7",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/KTpJnBIAAiWK",
		"status" : 1
	},
	{
		"idx" : 248,
		"title" : "까폼",
		"score" : "4.7",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/gxUqUtrD-IAa",
		"status" : 1
	},
	{
		"idx" : 249,
		"title" : "맛짱조개",
		"score" : "4.7",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/4hAcTcdILi",
		"status" : 1
	},
	{
		"idx" : 250,
		"title" : "빈호",
		"score" : "4.7",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/AqjtqrvjBdcg",
		"status" : 1
	},
	{
		"idx" : 251,
		"title" : "한상더테이블",
		"score" : "4.7",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/QdFQldFuby_V",
		"status" : 1
	},
	{
		"idx" : 252,
		"title" : "진미평양냉면",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/cTAy9QS_J5cl",
		"status" : 1
	},
	{
		"idx" : 253,
		"title" : "알라프리마",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/ByuIW33rXc",
		"status" : 1
	},
	{
		"idx" : 254,
		"title" : "가담",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/B8CzA6i9Bb8Z",
		"status" : 1
	},
	{
		"idx" : 255,
		"title" : "껠끄쇼즈",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/vcheyGIxPJ9D",
		"status" : 1
	},
	{
		"idx" : 256,
		"title" : "가디록",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/ol9BImtmnFqo",
		"status" : 1
	},
	{
		"idx" : 257,
		"title" : "마루심",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/KU-4QO6Yvt",
		"status" : 1
	},
	{
		"idx" : 258,
		"title" : "농민백암왕순대",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/vnc0i7l-fd",
		"status" : 1
	},
	{
		"idx" : 259,
		"title" : "롸카두들내쉬빌핫치킨",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/U1ONT3T0agK9",
		"status" : 1
	},
	{
		"idx" : 260,
		"title" : "카츠바이콘반",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/aPr-R4FpbnHO",
		"status" : 1
	},
	{
		"idx" : 261,
		"title" : "영동장어",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/QdnZnky2HnMJ",
		"status" : 1
	},
	{
		"idx" : 262,
		"title" : "엘레나영",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/2qUn7uv8lnGF",
		"status" : 1
	},
	{
		"idx" : 263,
		"title" : "갓포아키",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/8EGPzufM3i",
		"status" : 1
	},
	{
		"idx" : 264,
		"title" : "엘픽",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/RpEdp_TN6eZK",
		"status" : 1
	},
	{
		"idx" : 265,
		"title" : "고메램",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/WlCN9CJbEBwW",
		"status" : 1
	},
	{
		"idx" : 266,
		"title" : "스기타마",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/ozzOg8plVu4v",
		"status" : 1
	},
	{
		"idx" : 267,
		"title" : "위트앤미트",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/kZUywyY8DPyx",
		"status" : 1
	},
	{
		"idx" : 268,
		"title" : "더그레이트홍연",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/SECTJMGmMYY6",
		"status" : 1
	},
	{
		"idx" : 269,
		"title" : "우제홍참치",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/GsHC7WCEjX",
		"status" : 1
	},
	{
		"idx" : 270,
		"title" : "옥토스",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/9fX9iZIgEG7H",
		"status" : 1
	},
	{
		"idx" : 271,
		"title" : "왕스덕",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/5h2OL8a5GlY_",
		"status" : 1
	},
	{
		"idx" : 272,
		"title" : "양재초밥",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/LiZZB04VmzFP",
		"status" : 1
	},
	{
		"idx" : 273,
		"title" : "레아",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/qDj4t75-9IGS",
		"status" : 1
	},
	{
		"idx" : 274,
		"title" : "PIZZA PIZZA",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/jEqJYlWjkjpj",
		"status" : 1
	},
	{
		"idx" : 275,
		"title" : "레우레우",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/vsbpazqwbu7a",
		"status" : 1
	},
	{
		"idx" : 276,
		"title" : "계인전 보타니카",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/P7ZcLLOtU8wd",
		"status" : 1
	},
	{
		"idx" : 277,
		"title" : "이도",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/KF2fMgRyP4x4",
		"status" : 1
	},
	{
		"idx" : 278,
		"title" : "초록밭",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/hxAZ5cosM7lE",
		"status" : 1
	},
	{
		"idx" : 279,
		"title" : "큐리오",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/EzswfAaIvG1g",
		"status" : 1
	},
	{
		"idx" : 280,
		"title" : "김씨마구로",
		"score" : "4.5",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/OVsNBfEt9wSD",
		"status" : 1
	},
	{
		"idx" : 281,
		"title" : "슬로우치즈",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/TmKdK3zz6fQs",
		"status" : 1
	},
	{
		"idx" : 282,
		"title" : "Sogak",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/K1ujajEw-jUL",
		"status" : 1
	},
	{
		"idx" : 283,
		"title" : "일리조",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/ewTZ9Le7U54q",
		"status" : 1
	},
	{
		"idx" : 284,
		"title" : "원디그리노스",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/HXHddB8K6dak",
		"status" : 1
	},
	{
		"idx" : 285,
		"title" : "삐아프",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/QxTRZZv3Dl",
		"status" : 1
	},
	{
		"idx" : 286,
		"title" : "오향가",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/IGPyzMELa6",
		"status" : 1
	},
	{
		"idx" : 287,
		"title" : "인딕 슬로우",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/m16fiU1vHZhd",
		"status" : 1
	},
	{
		"idx" : 288,
		"title" : "스시렌",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/U2YxVAmkOVod",
		"status" : 1
	},
	{
		"idx" : 289,
		"title" : "해목",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/Rr3Nn2KvMQd-",
		"status" : 1
	},
	{
		"idx" : 290,
		"title" : "익스퀴진",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/nw_km_IuVW9l",
		"status" : 1
	},
	{
		"idx" : 291,
		"title" : "키겐",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/eEMujXaKYLRJ",
		"status" : 1
	},
	{
		"idx" : 292,
		"title" : "사브서울",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/dU0u62bWkZp1",
		"status" : 1
	},
	{
		"idx" : 293,
		"title" : "호시쿠",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/bC8zW90HKCh2",
		"status" : 1
	},
	{
		"idx" : 294,
		"title" : "신비갈비살",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/-EDDtVfafvaS",
		"status" : 1
	},
	{
		"idx" : 295,
		"title" : "무아",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/xDNDNLjcuw3J",
		"status" : 1
	},
	{
		"idx" : 296,
		"title" : "반티엔야오카오위",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/51t4XhhxEGpT",
		"status" : 1
	},
	{
		"idx" : 297,
		"title" : "쏭타이",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/rb3_HpDn7OXJ",
		"status" : 1
	},
	{
		"idx" : 298,
		"title" : "비네트",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/kgDrX5hPakLJ",
		"status" : 1
	},
	{
		"idx" : 299,
		"title" : "스시하쿠초",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/k0cLjaUIgspQ",
		"status" : 1
	},
	{
		"idx" : 300,
		"title" : "플랜튜드",
		"score" : "4.6",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/C1rSSjpEptN4",
		"status" : 1
	},
	{
		"idx" : 301,
		"title" : "강정이넘치는집",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/wT9UF1w_mNBh",
		"status" : 1
	},
	{
		"idx" : 302,
		"title" : "효계",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/7SfQFq6xnAuf",
		"status" : 1
	},
	{
		"idx" : 303,
		"title" : "양인환대",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/IJxA6CexwFwY",
		"status" : 1
	},
	{
		"idx" : 304,
		"title" : "은화계",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/LRlpXa9z4A6z",
		"status" : 1
	},
	{
		"idx" : 305,
		"title" : "돈불리제담",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/5KMjPZ-GFl",
		"status" : 1
	},
	{
		"idx" : 306,
		"title" : "이타닉가든",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/Bf0Kr8UFl6u0",
		"status" : 1
	},
	{
		"idx" : 307,
		"title" : "비스트로앤트로",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/VUQojbiMNMQm",
		"status" : 1
	},
	{
		"idx" : 308,
		"title" : "호별관",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/4MRu9Jsi1dxk",
		"status" : 1
	},
	{
		"idx" : 309,
		"title" : "FOURB",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/CkAjfohbdKuv",
		"status" : 1
	},
	{
		"idx" : 310,
		"title" : "티하우스하다",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/6IDQwmv2D9Nf",
		"status" : 1
	},
	{
		"idx" : 311,
		"title" : "B3713",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/HkRXWc3EiIgf",
		"status" : 1
	},
	{
		"idx" : 312,
		"title" : "야키토리파노",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/rONDlmEIowC8",
		"status" : 1
	},
	{
		"idx" : 313,
		"title" : "최가네버섯샤브매운탕칼국수",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/OduXGf6bwj",
		"status" : 1
	},
	{
		"idx" : 314,
		"title" : "하나샤부정",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/p-1rAzvY7V",
		"status" : 1
	},
	{
		"idx" : 315,
		"title" : "PDR",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/_u0AtWd2Sc7T",
		"status" : 1
	},
	{
		"idx" : 316,
		"title" : "고든램지 스트리트버거",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/YW6WsXTMbP_6",
		"status" : 1
	},
	{
		"idx" : 317,
		"title" : "논현장어",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/-ck3LyDmi2",
		"status" : 1
	},
	{
		"idx" : 318,
		"title" : "쿠시아게진",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/1uuzKojZK_mV",
		"status" : 1
	},
	{
		"idx" : 319,
		"title" : "오마치슌",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/hHWAZomPpzhQ",
		"status" : 1
	},
	{
		"idx" : 320,
		"title" : "브레덴버거",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/I3SMzk_CLKK_",
		"status" : 1
	},
	{
		"idx" : 321,
		"title" : "스시상현",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/WkH-RjnobiXE",
		"status" : 1
	},
	{
		"idx" : 322,
		"title" : "강남명전",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/TiUni946ZA8c",
		"status" : 1
	},
	{
		"idx" : 323,
		"title" : "트헝뜨",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/_P3pL0PHEvPw",
		"status" : 1
	},
	{
		"idx" : 324,
		"title" : "신사치킨클럽 (휴업중)",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/55JxAje9n9K9",
		"status" : 1
	},
	{
		"idx" : 325,
		"title" : "우밀면옥",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/tlWPASuCsTNS",
		"status" : 1
	},
	{
		"idx" : 326,
		"title" : "상석",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/cjqgzp6dKlZF",
		"status" : 1
	},
	{
		"idx" : 327,
		"title" : "갓포마코토",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/0VeeAq512q9s",
		"status" : 1
	},
	{
		"idx" : 328,
		"title" : "청우참치",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/YyRGx0QZRZ",
		"status" : 1
	},
	{
		"idx" : 329,
		"title" : "북해도목장",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/U4o5YOXR3Ys0",
		"status" : 1
	},
	{
		"idx" : 330,
		"title" : "히바치",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/5qlxMtyJLDMM",
		"status" : 1
	},
	{
		"idx" : 331,
		"title" : "아부라소바",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/8SzFocDsPq13",
		"status" : 1
	},
	{
		"idx" : 332,
		"title" : "구을가",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/1EXKzJGQ3IKy",
		"status" : 1
	},
	{
		"idx" : 333,
		"title" : "뻬를라",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/2EL8G-2KylF9",
		"status" : 1
	},
	{
		"idx" : 334,
		"title" : "코미도리",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/2wxAN0JGjcPx",
		"status" : 1
	},
	{
		"idx" : 335,
		"title" : "비스테까",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/SvMgRYjZHHS-",
		"status" : 1
	},
	{
		"idx" : 336,
		"title" : "동화고옥",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/a68YfUYU6TIe",
		"status" : 1
	},
	{
		"idx" : 337,
		"title" : "고꿉집",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/r_ZZReVfOdEM",
		"status" : 1
	},
	{
		"idx" : 338,
		"title" : "루자인",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/avjgCTVKT5Fx",
		"status" : 1
	},
	{
		"idx" : 339,
		"title" : "조선델리더부티크",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/Ps-9fhaJi-Ky",
		"status" : 1
	},
	{
		"idx" : 340,
		"title" : "보므청담",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/8geef_yXCLEA",
		"status" : 1
	},
	{
		"idx" : 341,
		"title" : "미우",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/0vQQ81qZCz8n",
		"status" : 1
	},
	{
		"idx" : 342,
		"title" : "임프레션",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/D9eg-mzX-gqZ",
		"status" : 1
	},
	{
		"idx" : 343,
		"title" : "시고로",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/FIxoQZOz_01C",
		"status" : 1
	},
	{
		"idx" : 344,
		"title" : "와려",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/3WdTi8o_WwC-",
		"status" : 1
	},
	{
		"idx" : 345,
		"title" : "더라운드",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/tvYBlZ3g8AYI",
		"status" : 1
	},
	{
		"idx" : 346,
		"title" : "소이연남마오",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/IxPgfbX7wag7",
		"status" : 1
	},
	{
		"idx" : 347,
		"title" : "뽕나무쟁이",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/mjR_ZoQd1e",
		"status" : 1
	},
	{
		"idx" : 348,
		"title" : "덕후선생",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/FfhZHT6Cc4Fk",
		"status" : 1
	},
	{
		"idx" : 349,
		"title" : "리북집",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/EbvI3yQuB2",
		"status" : 1
	},
	{
		"idx" : 350,
		"title" : "테일러커피",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/uiD1qcGYDC06",
		"status" : 1
	},
	{
		"idx" : 351,
		"title" : "원스타 올드패션드 햄버거",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/BQxl590Vix-Y",
		"status" : 1
	},
	{
		"idx" : 352,
		"title" : "스시하나레",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/AmUkJdUTGHIg",
		"status" : 1
	},
	{
		"idx" : 353,
		"title" : "야키토리묵",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/KWAbqJTAHmb-",
		"status" : 1
	},
	{
		"idx" : 354,
		"title" : "치즈룸",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/NgsGd9QAvtII",
		"status" : 1
	},
	{
		"idx" : 355,
		"title" : "제스트",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/8q085g_q1Pu4",
		"status" : 1
	},
	{
		"idx" : 356,
		"title" : "코지마",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/aCXcBYZL5K",
		"status" : 1
	},
	{
		"idx" : 357,
		"title" : "구테로이테",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/85X6w7IYsEEj",
		"status" : 1
	},
	{
		"idx" : 358,
		"title" : "외고집설렁탕",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/5HeqtDuK5R",
		"status" : 1
	},
	{
		"idx" : 359,
		"title" : "어물전 청",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/z8XeCpbf-VJb",
		"status" : 1
	},
	{
		"idx" : 360,
		"title" : "압구정공주떡집",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/Y5MLo2_mLa",
		"status" : 1
	},
	{
		"idx" : 361,
		"title" : "딜리셧부티끄",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/pWAvmqr2i7TE",
		"status" : 1
	},
	{
		"idx" : 362,
		"title" : "히노카츠",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/hJdDHIioDVEN",
		"status" : 1
	},
	{
		"idx" : 363,
		"title" : "가츠오",
		"score" : "4.4",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/N7J7PGaxTCK6",
		"status" : 1
	},
	{
		"idx" : 364,
		"title" : "정식당",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/KfToFUSQwI",
		"status" : 1
	},
	{
		"idx" : 365,
		"title" : "파이어벨",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/QPKEOPHiXM",
		"status" : 1
	},
	{
		"idx" : 366,
		"title" : "스와니예",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/eosoch5KLZ",
		"status" : 1
	},
	{
		"idx" : 367,
		"title" : "장스테이크",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/j8C1GHD2xA",
		"status" : 1
	},
	{
		"idx" : 368,
		"title" : "다운타우너",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/NjpKcKDN34oD",
		"status" : 1
	},
	{
		"idx" : 369,
		"title" : "리틀넥",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/R3iHj7sZaI",
		"status" : 1
	},
	{
		"idx" : 370,
		"title" : "바베네",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/YnDLhi_cWfgz",
		"status" : 1
	},
	{
		"idx" : 371,
		"title" : "로리스더프라임립",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/fBVd5rEQHN",
		"status" : 1
	},
	{
		"idx" : 372,
		"title" : "스시선수",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/P7NK0_5Krz",
		"status" : 1
	},
	{
		"idx" : 373,
		"title" : "김수사",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/tHu1pa6I3E",
		"status" : 1
	},
	{
		"idx" : 374,
		"title" : "부타이",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/gQUKnpHqDvPM",
		"status" : 1
	},
	{
		"idx" : 375,
		"title" : "뜨락",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/HcfgPb4E6D",
		"status" : 1
	},
	{
		"idx" : 376,
		"title" : "삼창교자",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/b7EeHUXUn7rz",
		"status" : 1
	},
	{
		"idx" : 377,
		"title" : "정돈",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/w_Uk02YqcI9h",
		"status" : 1
	},
	{
		"idx" : 378,
		"title" : "보타르가",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/FFEi7Xv1EVal",
		"status" : 1
	},
	{
		"idx" : 379,
		"title" : "스시 나미키",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/9TgE3uc7XPc6",
		"status" : 1
	},
	{
		"idx" : 380,
		"title" : "임병주산동칼국수",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/27_EgOQasf",
		"status" : 1
	},
	{
		"idx" : 381,
		"title" : "능라도",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/8HbnV3k0rX",
		"status" : 1
	},
	{
		"idx" : 382,
		"title" : "모찌방",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/2u-4-3abGwI4",
		"status" : 1
	},
	{
		"idx" : 383,
		"title" : "백년옥",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/_QTQ8AeF2j",
		"status" : 1
	},
	{
		"idx" : 384,
		"title" : "노란상소갈비",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/2l52up6B6MvY",
		"status" : 1
	},
	{
		"idx" : 385,
		"title" : "스시사카우",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/G6AgizCTtPC9",
		"status" : 1
	},
	{
		"idx" : 386,
		"title" : "몽중헌",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/n4N6o-A4zE",
		"status" : 1
	},
	{
		"idx" : 387,
		"title" : "스시 시미즈",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/lekDtZkiY1Cy",
		"status" : 1
	},
	{
		"idx" : 388,
		"title" : "광평 평양냉면갈비",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/OiGx5gttdCFM",
		"status" : 1
	},
	{
		"idx" : 389,
		"title" : "메종드라카테고리",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/uGja1CE039",
		"status" : 1
	},
	{
		"idx" : 390,
		"title" : "청류벽",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/HVICF2U7bp3e",
		"status" : 1
	},
	{
		"idx" : 391,
		"title" : "모범갈빗살",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/0Vq0bf1rZJLZ",
		"status" : 1
	},
	{
		"idx" : 392,
		"title" : "모터시티",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/g8HZjdy26NwR",
		"status" : 1
	},
	{
		"idx" : 393,
		"title" : "라미띠에",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/ERutA3IWve",
		"status" : 1
	},
	{
		"idx" : 394,
		"title" : "호루몬",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/YNrQYS-HUc9n",
		"status" : 1
	},
	{
		"idx" : 395,
		"title" : "베이크",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/JZM6HCHhwWoN",
		"status" : 1
	},
	{
		"idx" : 396,
		"title" : "일무레또",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/iGIG0xbXGn9Q",
		"status" : 1
	},
	{
		"idx" : 397,
		"title" : "고료리 켄",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/TznMMYOSqMQK",
		"status" : 1
	},
	{
		"idx" : 398,
		"title" : "파오파오",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/qJU5J5hrxX",
		"status" : 1
	},
	{
		"idx" : 399,
		"title" : "쎄쎄종",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/faOJKeUy00Yt",
		"status" : 1
	},
	{
		"idx" : 400,
		"title" : "하이디라오",
		"score" : "4.3",
		"region" : "강남",
		"url" : "https://www.mangoplate.com/restaurants/dKX9LuHmBLx0",
		"status" : 1
	},
	{
		"idx" : 401,
		"title" : "작은피자집",
		"score" : "4.7",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/A2wHyagv8QkV",
		"status" : 1
	},
	{
		"idx" : 402,
		"title" : "키세츠스시",
		"score" : "4.5",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/TVRfd2os48wZ",
		"status" : 1
	},
	{
		"idx" : 403,
		"title" : "서평면옥",
		"score" : "4.5",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/yhLPJnTWt17m",
		"status" : 1
	},
	{
		"idx" : 404,
		"title" : "산천칡냉면",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/1OmG5RPugq",
		"status" : 1
	},
	{
		"idx" : 405,
		"title" : "오다가다",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/hJd3wPlT-Hk_",
		"status" : 1
	},
	{
		"idx" : 406,
		"title" : "오센",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/aN3N2B6GKI",
		"status" : 1
	},
	{
		"idx" : 407,
		"title" : "우부래도",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/ADDZaJGhestM",
		"status" : 1
	},
	{
		"idx" : 408,
		"title" : "전주전집",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/OSIxmKY9vz",
		"status" : 1
	},
	{
		"idx" : 409,
		"title" : "브레드숨",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/dtgJuAt532",
		"status" : 1
	},
	{
		"idx" : 410,
		"title" : "프랑세즈",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/h1Ejl2vCEw",
		"status" : 1
	},
	{
		"idx" : 411,
		"title" : "서일순대국",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/ClicOh_9lt",
		"status" : 1
	},
	{
		"idx" : 412,
		"title" : "리얼후라이",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/JGMWqf-x5d",
		"status" : 1
	},
	{
		"idx" : 413,
		"title" : "미학당",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/-nEDN6dZrYGl",
		"status" : 1
	},
	{
		"idx" : 414,
		"title" : "두리닭발",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/K2apWGIrS4s9",
		"status" : 1
	},
	{
		"idx" : 415,
		"title" : "스톤504",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/_xAD1hC2TF",
		"status" : 1
	},
	{
		"idx" : 416,
		"title" : "정원분식",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/tLaYkhFcSOAn",
		"status" : 1
	},
	{
		"idx" : 417,
		"title" : "블랑제리꾸끄",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/x4v-MbAiG8z9",
		"status" : 1
	},
	{
		"idx" : 418,
		"title" : "마마부찌",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/4C6RGA9L3G",
		"status" : 1
	},
	{
		"idx" : 419,
		"title" : "올라아보",
		"score" : "4.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/8bMnQH_r40am",
		"status" : 1
	},
	{
		"idx" : 420,
		"title" : "운봉산장양고기전문점",
		"score" : "4.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/H7qgftiPmv",
		"status" : 1
	},
	{
		"idx" : 421,
		"title" : "하우스바이콘반",
		"score" : "4.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/2RWHSvPm2Rpz",
		"status" : 1
	},
	{
		"idx" : 422,
		"title" : "전라상회",
		"score" : "4.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/sBb2ypsWeE",
		"status" : 1
	},
	{
		"idx" : 423,
		"title" : "고우마구로",
		"score" : "4.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/Byd1b61IrXgG",
		"status" : 1
	},
	{
		"idx" : 424,
		"title" : "형제상회",
		"score" : "4.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/drXX2BDsGZ",
		"status" : 1
	},
	{
		"idx" : 425,
		"title" : "페니힐스커피스테이션",
		"score" : "4.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/RztxiJSWE4",
		"status" : 1
	},
	{
		"idx" : 426,
		"title" : "독도수산",
		"score" : "4.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/K1lhL2EtJRt8",
		"status" : 1
	},
	{
		"idx" : 427,
		"title" : "김씨마구로",
		"score" : "4.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/mseYsQL8gXuC",
		"status" : 1
	},
	{
		"idx" : 428,
		"title" : "가네끼스시",
		"score" : "4.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/u_FH24C5Kc",
		"status" : 1
	},
	{
		"idx" : 429,
		"title" : "다독이네 숯불구이",
		"score" : "4.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/NlrcpMeHFOzg",
		"status" : 1
	},
	{
		"idx" : 430,
		"title" : "맥파이앤타이거 신사티룸",
		"score" : "4.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/jEmQU2HkQdbh",
		"status" : 1
	},
	{
		"idx" : 431,
		"title" : "청양수산",
		"score" : "4.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/qv6OWyuV-5",
		"status" : 1
	},
	{
		"idx" : 432,
		"title" : "현고대닭발",
		"score" : "4.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/Xe6oNQt9a0",
		"status" : 1
	},
	{
		"idx" : 433,
		"title" : "일성수산",
		"score" : "4.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/ArOtFZjUZSg6",
		"status" : 1
	},
	{
		"idx" : 434,
		"title" : "공지안",
		"score" : "4.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/ooZCJSqe_c7G",
		"status" : 1
	},
	{
		"idx" : 435,
		"title" : "상남스시",
		"score" : "4.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/ycrMmagRkWil",
		"status" : 1
	},
	{
		"idx" : 436,
		"title" : "신사",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/P0wSfRAYsBcN",
		"status" : 1
	},
	{
		"idx" : 437,
		"title" : "뚜스뚜스",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/wO16uRuemcPp",
		"status" : 1
	},
	{
		"idx" : 438,
		"title" : "가춘",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/8dUdXFG9RH7d",
		"status" : 1
	},
	{
		"idx" : 439,
		"title" : "닭발집",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/IOpGKscCIN",
		"status" : 1
	},
	{
		"idx" : 440,
		"title" : "디피스트",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/p5mQ9DG5mPuA",
		"status" : 1
	},
	{
		"idx" : 441,
		"title" : "아는포차",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/DafFTh768N",
		"status" : 1
	},
	{
		"idx" : 442,
		"title" : "고추동제면소",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/NqhDANf431ay",
		"status" : 1
	},
	{
		"idx" : 443,
		"title" : "무삥과팟타이",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/rEIiocjsAA_f",
		"status" : 1
	},
	{
		"idx" : 444,
		"title" : "머치커피",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/EEQ95Ynqe0kI",
		"status" : 1
	},
	{
		"idx" : 445,
		"title" : "케이크팝",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/V1cplnv85_GB",
		"status" : 1
	},
	{
		"idx" : 446,
		"title" : "경성모밀",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/vvN7V3Sb2r_Q",
		"status" : 1
	},
	{
		"idx" : 447,
		"title" : "김재운초밥사랑",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/SGSYmzkcnyjW",
		"status" : 1
	},
	{
		"idx" : 448,
		"title" : "은희네온집닭떡볶이",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/BUgFz-BHGn3F",
		"status" : 1
	},
	{
		"idx" : 449,
		"title" : "시너리",
		"score" : "3.9",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/RBkkIMDaKcCi",
		"status" : 1
	},
	{
		"idx" : 450,
		"title" : "피터패트",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/fy45F1cT1Opt",
		"status" : 1
	},
	{
		"idx" : 451,
		"title" : "미스피츠",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/8GYdJoDk7KTu",
		"status" : 1
	},
	{
		"idx" : 452,
		"title" : "터방내",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/xUJDYH0K_E",
		"status" : 1
	},
	{
		"idx" : 453,
		"title" : "윤공KoreanBistro",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/Am96foCP-j3L",
		"status" : 1
	},
	{
		"idx" : 454,
		"title" : "사당모소리",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/DrqG-wTCEudO",
		"status" : 1
	},
	{
		"idx" : 455,
		"title" : "투디카페",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/0Ncua4FZxbZV",
		"status" : 1
	},
	{
		"idx" : 456,
		"title" : "칠기마라탕",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/NwXV4-Rw_81l",
		"status" : 1
	},
	{
		"idx" : 457,
		"title" : "Oomph",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/X_12rVKA4R-B",
		"status" : 1
	},
	{
		"idx" : 458,
		"title" : "양자호떡",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/SBHk7CABQFDh",
		"status" : 1
	},
	{
		"idx" : 459,
		"title" : "노량진할머니왕파전",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/TOi0JORtQs",
		"status" : 1
	},
	{
		"idx" : 460,
		"title" : "꿀꾸랄라",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/3W7mJ8UI6E",
		"status" : 1
	},
	{
		"idx" : 461,
		"title" : "칵토",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/ULjdFFHBURYk",
		"status" : 1
	},
	{
		"idx" : 462,
		"title" : "그릴진",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/MLyZwDnGobkB",
		"status" : 1
	},
	{
		"idx" : 463,
		"title" : "인근주민",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/eORTVpepmxT-",
		"status" : 1
	},
	{
		"idx" : 464,
		"title" : "애플하우스",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/47jYfj61kE",
		"status" : 1
	},
	{
		"idx" : 465,
		"title" : "초와밥",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/lVwSxatR9MQq",
		"status" : 1
	},
	{
		"idx" : 466,
		"title" : "브레드덕",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/ssiB5C0FPegV",
		"status" : 1
	},
	{
		"idx" : 467,
		"title" : "성민양꼬치",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/9U5TfS7QXj",
		"status" : 1
	},
	{
		"idx" : 468,
		"title" : "빈빈양꼬치",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/ktmEwLPH3N",
		"status" : 1
	},
	{
		"idx" : 469,
		"title" : "남궁야",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/6fRxhteqUR",
		"status" : 1
	},
	{
		"idx" : 470,
		"title" : "농부쌈밥",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/h7DVBeejtZ",
		"status" : 1
	},
	{
		"idx" : 471,
		"title" : "민이네식빵",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/n_8sMurr1a33",
		"status" : 1
	},
	{
		"idx" : 472,
		"title" : "텐카이치",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/QB6QIQTMPZTh",
		"status" : 1
	},
	{
		"idx" : 473,
		"title" : "방배한가람김밥",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/Nj2N9__vtUpG",
		"status" : 1
	},
	{
		"idx" : 474,
		"title" : "홍콩참치만두",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/L_E-mThwhbH6",
		"status" : 1
	},
	{
		"idx" : 475,
		"title" : "만경양육관",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/eAJhX63rrz",
		"status" : 1
	},
	{
		"idx" : 476,
		"title" : "파동추야",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/GF6jxs8luTct",
		"status" : 1
	},
	{
		"idx" : 477,
		"title" : "토크넌센스",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/kLSu0bmmdXbt",
		"status" : 1
	},
	{
		"idx" : 478,
		"title" : "리얼후라이",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/nOdxT5l2vP",
		"status" : 1
	},
	{
		"idx" : 479,
		"title" : "대박",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/1OVrnWYkmikK",
		"status" : 1
	},
	{
		"idx" : 480,
		"title" : "잔디속에있다고상상을해",
		"score" : "4.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/SxVZTQOwlbnk",
		"status" : 1
	},
	{
		"idx" : 481,
		"title" : "정작가의 막걸리집",
		"score" : "4.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/dFjEJPa93yJf",
		"status" : 1
	},
	{
		"idx" : 482,
		"title" : "오꼬노미스토리",
		"score" : "4.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/prl1JPZOWqag",
		"status" : 1
	},
	{
		"idx" : 483,
		"title" : "상도실내포장마차",
		"score" : "4.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/tH7GlUI0-_",
		"status" : 1
	},
	{
		"idx" : 484,
		"title" : "등나무집",
		"score" : "4.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/GK1ayhhScQ",
		"status" : 1
	},
	{
		"idx" : 485,
		"title" : "필수",
		"score" : "4.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/yKZZLpgiviHm",
		"status" : 1
	},
	{
		"idx" : 486,
		"title" : "팔각도",
		"score" : "4.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/XfPlAg7JFpCu",
		"status" : 1
	},
	{
		"idx" : 487,
		"title" : "스시로로",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/tRRYY79mpB",
		"status" : 1
	},
	{
		"idx" : 488,
		"title" : "릿잇타미",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/LULvqg_MUmTW",
		"status" : 1
	},
	{
		"idx" : 489,
		"title" : "리틀크레이지피자",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/AyeigDxaTh",
		"status" : 1
	},
	{
		"idx" : 490,
		"title" : "낯선한식븟다",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/TGp7SY8Xf0cf",
		"status" : 1
	},
	{
		"idx" : 491,
		"title" : "세시셀라팩토리",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/HlZE2ewV_F",
		"status" : 1
	},
	{
		"idx" : 492,
		"title" : "요란한부엌",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/cKhLhmAety3W",
		"status" : 1
	},
	{
		"idx" : 493,
		"title" : "사당광안리",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/hxvT6OzhZLrb",
		"status" : 1
	},
	{
		"idx" : 494,
		"title" : "사당돈",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/UvvuVIns9C5v",
		"status" : 1
	},
	{
		"idx" : 495,
		"title" : "쁘띠우스",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/lTLWGxebfanP",
		"status" : 1
	},
	{
		"idx" : 496,
		"title" : "재팔이네닭발",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/oWZ4cQgJ7FPV",
		"status" : 1
	},
	{
		"idx" : 497,
		"title" : "조가네갑오징어",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/GX0XMsW_3U",
		"status" : 1
	},
	{
		"idx" : 498,
		"title" : "와플스",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/pGFh5NflmoM3",
		"status" : 1
	},
	{
		"idx" : 499,
		"title" : "청와옥",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/EAKFIPyoZxUe",
		"status" : 1
	},
	{
		"idx" : 500,
		"title" : "가마솥손두부",
		"score" : "4.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/hVLHSCT8aE",
		"status" : 1
	},
	{
		"idx" : 501,
		"title" : "라시에스타",
		"score" : "3.6",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/cr7Ilv_cRQ0e",
		"status" : 1
	},
	{
		"idx" : 502,
		"title" : "오가네팬케이크",
		"score" : "3.6",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/5Fq3Fb-_h1",
		"status" : 1
	},
	{
		"idx" : 503,
		"title" : "낙성곱창",
		"score" : "3.6",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/-uivZIpFvI",
		"status" : 1
	},
	{
		"idx" : 504,
		"title" : "생어거스틴",
		"score" : "3.6",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/jyY4vffQ-J",
		"status" : 1
	},
	{
		"idx" : 505,
		"title" : "신이내린매운떡볶이",
		"score" : "3.6",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/68gMl3HiPX",
		"status" : 1
	},
	{
		"idx" : 506,
		"title" : "브루클린커피",
		"score" : "3.6",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/J1HNUEjwAwFb",
		"status" : 1
	},
	{
		"idx" : 507,
		"title" : "리에또",
		"score" : "2.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/FafFFxtgt8ip",
		"status" : 1
	},
	{
		"idx" : 508,
		"title" : "쟝블랑제리",
		"score" : "3.6",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/NsJqc3-q8cHM",
		"status" : 1
	},
	{
		"idx" : 509,
		"title" : "훈감동",
		"score" : "3.5",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/GFoJIAqR4XWV",
		"status" : 1
	},
	{
		"idx" : 510,
		"title" : "새우네집",
		"score" : "3.5",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/j8X7Bea6nUgx",
		"status" : 1
	},
	{
		"idx" : 511,
		"title" : "차녕식당",
		"score" : "3.5",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/OmuGTlni_r",
		"status" : 1
	},
	{
		"idx" : 512,
		"title" : "신짱스시",
		"score" : "3.5",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/NZz2M8mN7y5G",
		"status" : 1
	},
	{
		"idx" : 513,
		"title" : "상도곱창",
		"score" : "3.5",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/ha7d1FZIgr",
		"status" : 1
	},
	{
		"idx" : 514,
		"title" : "미구",
		"score" : "3.5",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/wfEWzvnPI3Rs",
		"status" : 1
	},
	{
		"idx" : 515,
		"title" : "라무진",
		"score" : "3.5",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/WhXtToU2lXEX",
		"status" : 1
	},
	{
		"idx" : 516,
		"title" : "시간을 들이다",
		"score" : "3.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/c4lqkgzJsxDo",
		"status" : 1
	},
	{
		"idx" : 517,
		"title" : "봉빌렛",
		"score" : "3.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/5k_zZMb5160m",
		"status" : 1
	},
	{
		"idx" : 518,
		"title" : "돈짱맛짱",
		"score" : "3.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/rIrU_Ku1vw",
		"status" : 1
	},
	{
		"idx" : 519,
		"title" : "장독대",
		"score" : "3.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/Ugha5LDGyA",
		"status" : 1
	},
	{
		"idx" : 520,
		"title" : "세시파스타",
		"score" : "3.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/dag1XjF6nrtG",
		"status" : 1
	},
	{
		"idx" : 521,
		"title" : "파니모들",
		"score" : "3.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/1Omq41XhPgdn",
		"status" : 1
	},
	{
		"idx" : 522,
		"title" : "피자보이시나",
		"score" : "3.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/eG4umSoMiypv",
		"status" : 1
	},
	{
		"idx" : 523,
		"title" : "바이슨버거",
		"score" : "3.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/2oVift1Mxcbl",
		"status" : 1
	},
	{
		"idx" : 524,
		"title" : "미묘라멘",
		"score" : "3.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/TTg8fkxnYsc5",
		"status" : 1
	},
	{
		"idx" : 525,
		"title" : "킨로우라멘",
		"score" : "3.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/xjKc57BQilyV",
		"status" : 1
	},
	{
		"idx" : 526,
		"title" : "소담촌",
		"score" : "3.4",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/bRoIGnYbVWY8",
		"status" : 1
	},
	{
		"idx" : 527,
		"title" : "올리브에비뉴",
		"score" : "3.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/QI2VXLwWLS",
		"status" : 1
	},
	{
		"idx" : 528,
		"title" : "청년다방",
		"score" : "3.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/TUlbVIqHTkye",
		"status" : 1
	},
	{
		"idx" : 529,
		"title" : "피맥하우스",
		"score" : "3.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/u2o_2ZVlX_d2",
		"status" : 1
	},
	{
		"idx" : 530,
		"title" : "은행골",
		"score" : "3.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/D7TKfWhAPjb1",
		"status" : 1
	},
	{
		"idx" : 531,
		"title" : "라화방",
		"score" : "3.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/os0fS54hL2Sa",
		"status" : 1
	},
	{
		"idx" : 532,
		"title" : "이수회관",
		"score" : "3.3",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/pajCmB6mhs7p",
		"status" : 1
	},
	{
		"idx" : 533,
		"title" : "계탄언니",
		"score" : "3.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/WaxAt_QZpi5X",
		"status" : 1
	},
	{
		"idx" : 534,
		"title" : "카페페라",
		"score" : "3.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/8MzKxtyUXr",
		"status" : 1
	},
	{
		"idx" : 535,
		"title" : "복돈이부추삼겹살",
		"score" : "3.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/dRqKsJbsWW",
		"status" : 1
	},
	{
		"idx" : 536,
		"title" : "세녹",
		"score" : "3.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/hpV-zv_Mf3nT",
		"status" : 1
	},
	{
		"idx" : 537,
		"title" : "닥터로빈",
		"score" : "3.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/CExiY5rz2O",
		"status" : 1
	},
	{
		"idx" : 538,
		"title" : "매드포갈릭",
		"score" : "3.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/6D0pswgqrp",
		"status" : 1
	},
	{
		"idx" : 539,
		"title" : "72420",
		"score" : "3.2",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/WL3ljUWsG5X0",
		"status" : 1
	},
	{
		"idx" : 540,
		"title" : "빕스",
		"score" : "3.1",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/SLhixDvXTR",
		"status" : 1
	},
	{
		"idx" : 541,
		"title" : "도쿄빙수",
		"score" : "3.0",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/lBuvNyMn37Mo",
		"status" : 1
	},
	{
		"idx" : 542,
		"title" : "카페브르브르",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/fJh1Mo2u2Pgv",
		"status" : 1
	},
	{
		"idx" : 543,
		"title" : "즉석바지락손칼국수",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/bfMxPkzeEu",
		"status" : 1
	},
	{
		"idx" : 544,
		"title" : "마왕족발",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/WcLEwSo-wUd6",
		"status" : 1
	},
	{
		"idx" : 545,
		"title" : "피자보이시나",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/ZY1VJTDUrd7y",
		"status" : 1
	},
	{
		"idx" : 546,
		"title" : "당진수산",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/F2cTW_GI8wvI",
		"status" : 1
	},
	{
		"idx" : 547,
		"title" : "모든것은당근케이크에서시작됐다",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/ZoOw5oV-AEeu",
		"status" : 1
	},
	{
		"idx" : 548,
		"title" : "오드리곱창",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/yPznlHb7d3i3",
		"status" : 1
	},
	{
		"idx" : 549,
		"title" : "시에나에스프레소",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/CPCpIfAJ6meo",
		"status" : 1
	},
	{
		"idx" : 550,
		"title" : "계림원",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/NtAu9D6Q5I",
		"status" : 1
	},
	{
		"idx" : 551,
		"title" : "꿀때기곱창",
		"score" : "3.8",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/nIAGBjBBb_7C",
		"status" : 1
	},
	{
		"idx" : 552,
		"title" : "사이공리",
		"score" : "3.7",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/hEb89Uy5VaI-",
		"status" : 1
	},
	{
		"idx" : 553,
		"title" : "프라이밋 스테이크하우스",
		"score" : "3.7",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/IuUOoNXhslpJ",
		"status" : 1
	},
	{
		"idx" : 554,
		"title" : "방배김밥",
		"score" : "3.7",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/Renrm4O5tW",
		"status" : 1
	},
	{
		"idx" : 555,
		"title" : "곱창의전설",
		"score" : "3.7",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/ypqGF-bu0x",
		"status" : 1
	},
	{
		"idx" : 556,
		"title" : "정애맛담",
		"score" : "3.7",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/GCfHdWstpHJg",
		"status" : 1
	},
	{
		"idx" : 557,
		"title" : "진상천",
		"score" : "3.7",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/rhu-1piIbp8u",
		"status" : 1
	},
	{
		"idx" : 558,
		"title" : "바르미샤브샤브앤칼국수",
		"score" : "3.7",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/vApeJi2L8U",
		"status" : 1
	},
	{
		"idx" : 559,
		"title" : "삼삼가마솥돈까스 앤 칡불냉면",
		"score" : "3.7",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/TGbBLOqKdmxX",
		"status" : 1
	},
	{
		"idx" : 560,
		"title" : "장수원",
		"score" : "3.6",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/yEDbbkEVWb",
		"status" : 1
	},
	{
		"idx" : 561,
		"title" : "오후홍콩",
		"score" : "3.6",
		"region" : "동작/사당",
		"url" : "https://www.mangoplate.com/restaurants/kCsGb6y9lGNC",
		"status" : 1
	},
	{
		"idx" : 562,
		"title" : "고로커피로스터스",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/xcWGflpJXnyA",
		"status" : 1
	},
	{
		"idx" : 563,
		"title" : "통영장어잡는날",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/B2N2eT0jL3",
		"status" : 1
	},
	{
		"idx" : 564,
		"title" : "표표마라탕",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/gaq7KXqUuyv2",
		"status" : 1
	},
	{
		"idx" : 565,
		"title" : "조선펍에디",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/ePyGCxVes7i2",
		"status" : 1
	},
	{
		"idx" : 566,
		"title" : "하라고지페",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/mo-JoHjUF0ed",
		"status" : 1
	},
	{
		"idx" : 567,
		"title" : "오첨지",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/pS4G5e128O",
		"status" : 1
	},
	{
		"idx" : 568,
		"title" : "앤미",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/YlViXo4edYsB",
		"status" : 1
	},
	{
		"idx" : 569,
		"title" : "세월마차",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/kxw9aVXgpgJl",
		"status" : 1
	},
	{
		"idx" : 570,
		"title" : "화상손만두",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/xkvVRkJHFbmV",
		"status" : 1
	},
	{
		"idx" : 571,
		"title" : "그릭데이",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/X5eJZ-c5beL8",
		"status" : 1
	},
	{
		"idx" : 572,
		"title" : "리버벨",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/GucCY0UuPvWZ",
		"status" : 1
	},
	{
		"idx" : 573,
		"title" : "발루토",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/cWfAVTOfVdLb",
		"status" : 1
	},
	{
		"idx" : 574,
		"title" : "온고지신",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/OtI3U1CQpS0v",
		"status" : 1
	},
	{
		"idx" : 575,
		"title" : "프랑스홍합집",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/VbVnWwnkwamE",
		"status" : 1
	},
	{
		"idx" : 576,
		"title" : "막불감동",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/hdeyUljHK5o6",
		"status" : 1
	},
	{
		"idx" : 577,
		"title" : "십장생베이커리",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/fnsB3SDKAL5c",
		"status" : 1
	},
	{
		"idx" : 578,
		"title" : "초와밥",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Ft_s1us7Pg90",
		"status" : 1
	},
	{
		"idx" : 579,
		"title" : "삼촌네",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/W7QiHQonSe",
		"status" : 1
	},
	{
		"idx" : 580,
		"title" : "다케",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/-C1tadV-lA",
		"status" : 1
	},
	{
		"idx" : 581,
		"title" : "카페녹다",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/F8-C5qGLGfgc",
		"status" : 1
	},
	{
		"idx" : 582,
		"title" : "스톡홀름샐러드",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/my8u04eDDDLH",
		"status" : 1
	},
	{
		"idx" : 583,
		"title" : "나인온스버거",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/SLOZsg9Mlw",
		"status" : 1
	},
	{
		"idx" : 584,
		"title" : "옷살",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/mMDmU4jdnb",
		"status" : 1
	},
	{
		"idx" : 585,
		"title" : "더은교 (휴업중)",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/DqzNJqbESJ",
		"status" : 1
	},
	{
		"idx" : 586,
		"title" : "킷사서울",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/ZGOeVh-Al5ER",
		"status" : 1
	},
	{
		"idx" : 587,
		"title" : "외래향",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/2YD5fgUoUa",
		"status" : 1
	},
	{
		"idx" : 588,
		"title" : "기절초풍왕순대",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/JLY7RNzJTTlr",
		"status" : 1
	},
	{
		"idx" : 589,
		"title" : "산골",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/bJYOm7MjWPoX",
		"status" : 1
	},
	{
		"idx" : 590,
		"title" : "타이패밀리",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/FPcGRaIKJ1wZ",
		"status" : 1
	},
	{
		"idx" : 591,
		"title" : "정숙성",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/sC1kpSEK-lQ1",
		"status" : 1
	},
	{
		"idx" : 592,
		"title" : "사케바히토리",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/oP7kO6xCIoNv",
		"status" : 1
	},
	{
		"idx" : 593,
		"title" : "두리닭발",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/K2apWGIrS4s9",
		"status" : 1
	},
	{
		"idx" : 594,
		"title" : "축상",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/swLEKBUAt0Ie",
		"status" : 1
	},
	{
		"idx" : 595,
		"title" : "맨프럼오키나와",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/p51Uldzjd5iz",
		"status" : 1
	},
	{
		"idx" : 596,
		"title" : "앙뿌",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/H6A_NzyizccI",
		"status" : 1
	},
	{
		"idx" : 597,
		"title" : "메밀쟁이",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/51WSXfrLk2Du",
		"status" : 1
	},
	{
		"idx" : 598,
		"title" : "서랍",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/gWYmQP0YUcHE",
		"status" : 1
	},
	{
		"idx" : 599,
		"title" : "완산정",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/OowMCwlh4b",
		"status" : 1
	},
	{
		"idx" : 600,
		"title" : "로향양꼬치",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Tlnsd2swpFF6",
		"status" : 1
	},
	{
		"idx" : 601,
		"title" : "논밭골",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/KTMegSkFTv",
		"status" : 1
	},
	{
		"idx" : 602,
		"title" : "라이라이켄",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/LvPDBGH9TWwg",
		"status" : 1
	},
	{
		"idx" : 603,
		"title" : "커피볶는여자",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/KIjjCOGG794g",
		"status" : 1
	},
	{
		"idx" : 604,
		"title" : "딸랏롯빠이",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/ZwA1n6OT5GpV",
		"status" : 1
	},
	{
		"idx" : 605,
		"title" : "동학",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/N6zsknPkBG5l",
		"status" : 1
	},
	{
		"idx" : 606,
		"title" : "안밀",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/DSegyNnwAC2u",
		"status" : 1
	},
	{
		"idx" : 607,
		"title" : "춘천골참숯불닭갈비",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/A3itRxUfBs",
		"status" : 1
	},
	{
		"idx" : 608,
		"title" : "누아젯",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/_j3A0ar-GYFj",
		"status" : 1
	},
	{
		"idx" : 609,
		"title" : "테일오브테일스",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/dwqcRR5piT3Z",
		"status" : 1
	},
	{
		"idx" : 610,
		"title" : "피자보이시나",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/pVydRWGId3d8",
		"status" : 1
	},
	{
		"idx" : 611,
		"title" : "우리동네고기집",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/OU8Cm3Z-5R",
		"status" : 1
	},
	{
		"idx" : 612,
		"title" : "삼차",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/0V1-u8BKynNk",
		"status" : 1
	},
	{
		"idx" : 613,
		"title" : "Swirling",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/LjXdwsOynI_u",
		"status" : 1
	},
	{
		"idx" : 614,
		"title" : "오지 편한식당",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/P34gLPnn-BhC",
		"status" : 1
	},
	{
		"idx" : 615,
		"title" : "더멜팅팟",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/_nHzh3wxgz8w",
		"status" : 1
	},
	{
		"idx" : 616,
		"title" : "푀유 파티세리",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/g0N_jDu7tyvV",
		"status" : 1
	},
	{
		"idx" : 617,
		"title" : "투머트",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/OJwUFWlHX6qf",
		"status" : 1
	},
	{
		"idx" : 618,
		"title" : "정담은보쌈",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/K7GrMc9Taz",
		"status" : 1
	},
	{
		"idx" : 619,
		"title" : "봉이돈가스",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/wgnfZ9fV8Zqu",
		"status" : 1
	},
	{
		"idx" : 620,
		"title" : "낀알로이알로이",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/-WulDjRxRV1s",
		"status" : 1
	},
	{
		"idx" : 621,
		"title" : "소미당",
		"score" : "4.1",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/P_0ncHUU8dv6",
		"status" : 1
	},
	{
		"idx" : 622,
		"title" : "베이컨시",
		"score" : "4.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/naO5C9wSDnbr",
		"status" : 1
	},
	{
		"idx" : 623,
		"title" : "루비정",
		"score" : "4.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/XfzJkDiMjqDu",
		"status" : 1
	},
	{
		"idx" : 624,
		"title" : "따빠디또 디저트 따빠스바",
		"score" : "4.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Fy2Z5kqgi-7b",
		"status" : 1
	},
	{
		"idx" : 625,
		"title" : "뉴욕택시디저트",
		"score" : "4.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/XRoMziImmYCC",
		"status" : 1
	},
	{
		"idx" : 626,
		"title" : "오월의김밥",
		"score" : "4.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/q1PDtSFDsXea",
		"status" : 1
	},
	{
		"idx" : 627,
		"title" : "빠사삭튀김포차",
		"score" : "4.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/CbdJqQErxKsX",
		"status" : 1
	},
	{
		"idx" : 628,
		"title" : "두만강샤브샤브",
		"score" : "4.4",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/56MKQk5Vm_",
		"status" : 1
	},
	{
		"idx" : 629,
		"title" : "퍼블리코타코",
		"score" : "4.4",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/y4pGEk_ZwDqZ",
		"status" : 1
	},
	{
		"idx" : 630,
		"title" : "로향양꼬치",
		"score" : "4.4",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/3A0Z-gBcPl",
		"status" : 1
	},
	{
		"idx" : 631,
		"title" : "카츠오도",
		"score" : "4.4",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/IMY5hLfLjXgs",
		"status" : 1
	},
	{
		"idx" : 632,
		"title" : "쟝블랑제리",
		"score" : "4.3",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/J4rryjvWN5",
		"status" : 1
	},
	{
		"idx" : 633,
		"title" : "동경산책",
		"score" : "4.3",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/bKBEWmF8MVGb",
		"status" : 1
	},
	{
		"idx" : 634,
		"title" : "제주상회",
		"score" : "4.3",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/t6HIMLUBEg-_",
		"status" : 1
	},
	{
		"idx" : 635,
		"title" : "크래프티",
		"score" : "4.3",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Y4DpD3wFYBeb",
		"status" : 1
	},
	{
		"idx" : 636,
		"title" : "서울갈비",
		"score" : "4.3",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/DuYISQu8X9",
		"status" : 1
	},
	{
		"idx" : 637,
		"title" : "청송산오징어",
		"score" : "4.3",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/UIp8NwSb6Y",
		"status" : 1
	},
	{
		"idx" : 638,
		"title" : "요샌",
		"score" : "4.3",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Jy5r57U9CpfX",
		"status" : 1
	},
	{
		"idx" : 639,
		"title" : "어부사시가",
		"score" : "4.3",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/aSyhbUghoXti",
		"status" : 1
	},
	{
		"idx" : 640,
		"title" : "키요이스키야키",
		"score" : "4.3",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/mPvhcMuGK5e3",
		"status" : 1
	},
	{
		"idx" : 641,
		"title" : "텐동요츠야",
		"score" : "4.2",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/A5O1smA6kZGW",
		"status" : 1
	},
	{
		"idx" : 642,
		"title" : "가람숙성대광어",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/cnTcixR-H7zk",
		"status" : 1
	},
	{
		"idx" : 643,
		"title" : "아리차이",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/hX0tke6m83",
		"status" : 1
	},
	{
		"idx" : 644,
		"title" : "가네샤",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/ZknfMajVJu",
		"status" : 1
	},
	{
		"idx" : 645,
		"title" : "중화요리팔공",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/HoWked2wivcI",
		"status" : 1
	},
	{
		"idx" : 646,
		"title" : "사담",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Ibus9GLVMyRD",
		"status" : 1
	},
	{
		"idx" : 647,
		"title" : "하정식당",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/q4Kf3Hiu-8Xo",
		"status" : 1
	},
	{
		"idx" : 648,
		"title" : "마뇨떡볶이",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/s5pHAbDq_71M",
		"status" : 1
	},
	{
		"idx" : 649,
		"title" : "섭지수산",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/8rNMGFy8vcPL",
		"status" : 1
	},
	{
		"idx" : 650,
		"title" : "리앙크리스피롤",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/s0G5Q_dfpNLJ",
		"status" : 1
	},
	{
		"idx" : 651,
		"title" : "가츠가게",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/lfvQ_vOXxJ9g",
		"status" : 1
	},
	{
		"idx" : 652,
		"title" : "다이히로",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/FoLbCqh9_edJ",
		"status" : 1
	},
	{
		"idx" : 653,
		"title" : "카페청신호",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/NGI9HDXp5Qin",
		"status" : 1
	},
	{
		"idx" : 654,
		"title" : "만경양육관",
		"score" : "4.0",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/eAJhX63rrz",
		"status" : 1
	},
	{
		"idx" : 655,
		"title" : "쥬벤쿠바",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Dneh4RAi-r6Z",
		"status" : 1
	},
	{
		"idx" : 656,
		"title" : "아모르미오",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/21iZyNa7uT",
		"status" : 1
	},
	{
		"idx" : 657,
		"title" : "모즈타파스라운지",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/C9tYz1S8yHaf",
		"status" : 1
	},
	{
		"idx" : 658,
		"title" : "분짜 하노이",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/ak4N5gZLEb-w",
		"status" : 1
	},
	{
		"idx" : 659,
		"title" : "차이나당",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/9KocgR_GYI",
		"status" : 1
	},
	{
		"idx" : 660,
		"title" : "반조",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/euMu8zxKZaiV",
		"status" : 1
	},
	{
		"idx" : 661,
		"title" : "무삥과팟타이",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/mbMFJrE7XTmy",
		"status" : 1
	},
	{
		"idx" : 662,
		"title" : "고명집",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/fLxqaQ-2EB",
		"status" : 1
	},
	{
		"idx" : 663,
		"title" : "티라노",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/T6xNteFaD3",
		"status" : 1
	},
	{
		"idx" : 664,
		"title" : "행운당",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/V2HXdhgyDCXA",
		"status" : 1
	},
	{
		"idx" : 665,
		"title" : "만석곱창구이",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/LV0gG9qlcFks",
		"status" : 1
	},
	{
		"idx" : 666,
		"title" : "스시스캔들",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/vOrDyqyGwKoq",
		"status" : 1
	},
	{
		"idx" : 667,
		"title" : "카페프레임",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/VZ5JU6FYC0zj",
		"status" : 1
	},
	{
		"idx" : 668,
		"title" : "라우더커피바",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/sb78n1cFwATm",
		"status" : 1
	},
	{
		"idx" : 669,
		"title" : "관악관",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/qRdf2CowqT5w",
		"status" : 1
	},
	{
		"idx" : 670,
		"title" : "토모",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/grwo9LHse4",
		"status" : 1
	},
	{
		"idx" : 671,
		"title" : "달첨시루",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/LF4umbgg_s9u",
		"status" : 1
	},
	{
		"idx" : 672,
		"title" : "전주익산",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Sy-g63aKuv",
		"status" : 1
	},
	{
		"idx" : 673,
		"title" : "제일공간",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/MOB25X1DYUgq",
		"status" : 1
	},
	{
		"idx" : 674,
		"title" : "우리가참순대",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/JfRLz7Sbn2A1",
		"status" : 1
	},
	{
		"idx" : 675,
		"title" : "이야기",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/vluVwignNS",
		"status" : 1
	},
	{
		"idx" : 676,
		"title" : "포포인",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/ULAdqzInt8GJ",
		"status" : 1
	},
	{
		"idx" : 677,
		"title" : "엔조",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/lXEvdICt8G",
		"status" : 1
	},
	{
		"idx" : 678,
		"title" : "분미",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Y8QpUb2dKxi0",
		"status" : 1
	},
	{
		"idx" : 679,
		"title" : "쿠버타코멕시칸펍",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/rJf6MdLTP3EJ",
		"status" : 1
	},
	{
		"idx" : 680,
		"title" : "니와",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/WdHhItZ1AJ",
		"status" : 1
	},
	{
		"idx" : 681,
		"title" : "월화고기",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/pm-Tbo18zGXT",
		"status" : 1
	},
	{
		"idx" : 682,
		"title" : "온돌",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/O3G5N6Lrh8mX",
		"status" : 1
	},
	{
		"idx" : 683,
		"title" : "성민양꼬치",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/ssn03vG7vm",
		"status" : 1
	},
	{
		"idx" : 684,
		"title" : "프로젝트서울",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/81kWd-H_zGnK",
		"status" : 1
	},
	{
		"idx" : 685,
		"title" : "파고",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/iQsS7AyAhEqK",
		"status" : 1
	},
	{
		"idx" : 686,
		"title" : "포도원삼계탕",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/hGYAz5kCSu",
		"status" : 1
	},
	{
		"idx" : 687,
		"title" : "OFFOF카페",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/L8sVwCibtwzi",
		"status" : 1
	},
	{
		"idx" : 688,
		"title" : "더로스터59",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/XfVYXqSVPHIA",
		"status" : 1
	},
	{
		"idx" : 689,
		"title" : "어메이징디",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/8rPm-WsqRnHs",
		"status" : 1
	},
	{
		"idx" : 690,
		"title" : "오후의과일",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/neMSsHtySCvG",
		"status" : 1
	},
	{
		"idx" : 691,
		"title" : "만두작만두작",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/uBFFpvGc9Y7r",
		"status" : 1
	},
	{
		"idx" : 692,
		"title" : "얹다",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/O859JBiRsjFK",
		"status" : 1
	},
	{
		"idx" : 693,
		"title" : "마차이짬뽕",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/mD-Gyw0snTjm",
		"status" : 1
	},
	{
		"idx" : 694,
		"title" : "덕봉식당",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/tWocWnJcDl0h",
		"status" : 1
	},
	{
		"idx" : 695,
		"title" : "카페폴",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/L8CEiK3x9VGn",
		"status" : 1
	},
	{
		"idx" : 696,
		"title" : "야간얼큰우동",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/AK-G4yUgDmCP",
		"status" : 1
	},
	{
		"idx" : 697,
		"title" : "씨크스페셜티커피",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/SHdJCMLq0PuG",
		"status" : 1
	},
	{
		"idx" : 698,
		"title" : "카페미뇽",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/DGMCxHK8Gigc",
		"status" : 1
	},
	{
		"idx" : 699,
		"title" : "황토방",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/ucuKBbQauW",
		"status" : 1
	},
	{
		"idx" : 700,
		"title" : "자하연식당",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/aOdvm-R9hxvm",
		"status" : 1
	},
	{
		"idx" : 701,
		"title" : "르브와",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/vjwrw3WPMR",
		"status" : 1
	},
	{
		"idx" : 702,
		"title" : "모힝",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/ROf4X-Jzrn",
		"status" : 1
	},
	{
		"idx" : 703,
		"title" : "메이드바이아린",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/zjzaDoo03R3Q",
		"status" : 1
	},
	{
		"idx" : 704,
		"title" : "순보보",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/nuc6Yvm70E",
		"status" : 1
	},
	{
		"idx" : 705,
		"title" : "만성찬팅",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/6d5df4lJByD6",
		"status" : 1
	},
	{
		"idx" : 706,
		"title" : "꼬르동",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/OeRBgctdGxeT",
		"status" : 1
	},
	{
		"idx" : 707,
		"title" : "레그나나폴리",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/kD4p92vu0JgC",
		"status" : 1
	},
	{
		"idx" : 708,
		"title" : "안녕부산",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/cbdVAvBT1gsD",
		"status" : 1
	},
	{
		"idx" : 709,
		"title" : "웨어아위",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/r1HU-66k-AJU",
		"status" : 1
	},
	{
		"idx" : 710,
		"title" : "쑥고개",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/6BQvGmqcqC0_",
		"status" : 1
	},
	{
		"idx" : 711,
		"title" : "종로계림닭도리탕원조",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/GMrqDuBpT84l",
		"status" : 1
	},
	{
		"idx" : 712,
		"title" : "시골집",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Mqj8Ajdy87",
		"status" : 1
	},
	{
		"idx" : 713,
		"title" : "청기와타운",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/VYQymFf5v_Xm",
		"status" : 1
	},
	{
		"idx" : 714,
		"title" : "코시롱",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/CNFpjMrPFo9m",
		"status" : 1
	},
	{
		"idx" : 715,
		"title" : "생각보다맛있는집",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/H4ywyfvygf",
		"status" : 1
	},
	{
		"idx" : 716,
		"title" : "남도반주",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Y21OHIkIPpMF",
		"status" : 1
	},
	{
		"idx" : 717,
		"title" : "신촌황소곱창",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/-EyZPdLrx-",
		"status" : 1
	},
	{
		"idx" : 718,
		"title" : "오른손푸드카페",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/nbLmrSm30q8M",
		"status" : 1
	},
	{
		"idx" : 719,
		"title" : "펠리치따",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/RaiFTp6CPjiB",
		"status" : 1
	},
	{
		"idx" : 720,
		"title" : "아마",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/qwsqwCxQSJ-b",
		"status" : 1
	},
	{
		"idx" : 721,
		"title" : "디자이너리카페",
		"score" : "3.7",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/eBkFCL4YGitL",
		"status" : 1
	},
	{
		"idx" : 722,
		"title" : "수상한닭발",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/y4n_Hg-Xoo",
		"status" : 1
	},
	{
		"idx" : 723,
		"title" : "곳간집",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/lbQi6p1iADL4",
		"status" : 1
	},
	{
		"idx" : 724,
		"title" : "아로이팟타이",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/hZ3576V1w1At",
		"status" : 1
	},
	{
		"idx" : 725,
		"title" : "혼네",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/L4Nfc9rycyqr",
		"status" : 1
	},
	{
		"idx" : 726,
		"title" : "신림동피자집",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/RW7UpZAkatp2",
		"status" : 1
	},
	{
		"idx" : 727,
		"title" : "예인촌막걸리",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/l5NrOMOoUFJT",
		"status" : 1
	},
	{
		"idx" : 728,
		"title" : "고모네정육식당",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/bgbs23fGlnTp",
		"status" : 1
	},
	{
		"idx" : 729,
		"title" : "얼큰수제비해물칼국수",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/4hfaGPn9Ms",
		"status" : 1
	},
	{
		"idx" : 730,
		"title" : "에르디",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/xBT6aBAETl4q",
		"status" : 1
	},
	{
		"idx" : 731,
		"title" : "별이오름",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/DzalRBTSC067",
		"status" : 1
	},
	{
		"idx" : 732,
		"title" : "고베그릴",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/37-mXQwXHS",
		"status" : 1
	},
	{
		"idx" : 733,
		"title" : "츠루츠루",
		"score" : "3.9",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/NUZHv9Kt40Ep",
		"status" : 1
	},
	{
		"idx" : 734,
		"title" : "려",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/6U4hCwocdA",
		"status" : 1
	},
	{
		"idx" : 735,
		"title" : "엘따뻬오",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/oZ7xjAZ2H3px",
		"status" : 1
	},
	{
		"idx" : 736,
		"title" : "모힝",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/RH2Pb2l-b2",
		"status" : 1
	},
	{
		"idx" : 737,
		"title" : "낭만모로코",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/oJxHU8zUmofk",
		"status" : 1
	},
	{
		"idx" : 738,
		"title" : "아띠85도씨베이커리",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/ILtVD51fTA",
		"status" : 1
	},
	{
		"idx" : 739,
		"title" : "박명주브라더",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/IixoQzFRhx7V",
		"status" : 1
	},
	{
		"idx" : 740,
		"title" : "링고",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/0tR9NIFNPf9A",
		"status" : 1
	},
	{
		"idx" : 741,
		"title" : "바닐라스카이",
		"score" : "3.8",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/FTRmlvu0ld",
		"status" : 1
	},
	{
		"idx" : 742,
		"title" : "숙이네조개전골",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/FbsjXi2hWVy5",
		"status" : 1
	},
	{
		"idx" : 743,
		"title" : "더랩 24 7",
		"score" : "3.6",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/IME3tD7ekwGZ",
		"status" : 1
	},
	{
		"idx" : 744,
		"title" : "안녕과자점",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Z5ZdI83yF9Cy",
		"status" : 1
	},
	{
		"idx" : 745,
		"title" : "토끼네마굿간",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/VoZH5s5ioo9v",
		"status" : 1
	},
	{
		"idx" : 746,
		"title" : "몽중인",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/ybsiG_1IiSI1",
		"status" : 1
	},
	{
		"idx" : 747,
		"title" : "모리돈부리",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/RG5A_kb_8d",
		"status" : 1
	},
	{
		"idx" : 748,
		"title" : "김창일스시",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/Jubb943W0JUt",
		"status" : 1
	},
	{
		"idx" : 749,
		"title" : "데일리오아시스",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/aORPtkNdQM7m",
		"status" : 1
	},
	{
		"idx" : 750,
		"title" : "라페리체",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/7QX7ng-KicNj",
		"status" : 1
	},
	{
		"idx" : 751,
		"title" : "우디가스트로",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/NuGQ2te1JvyN",
		"status" : 1
	},
	{
		"idx" : 752,
		"title" : "멘쇼우라멘",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/-WO41j8a03hT",
		"status" : 1
	},
	{
		"idx" : 753,
		"title" : "서울뼛국",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/vCeS8OwViYnd",
		"status" : 1
	},
	{
		"idx" : 754,
		"title" : "미친키친",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/NmyzRJR2vqOg",
		"status" : 1
	},
	{
		"idx" : 755,
		"title" : "신기루황소곱창",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/euWv0gsgSI",
		"status" : 1
	},
	{
		"idx" : 756,
		"title" : "라공방",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/8OsiSvzAEKNt",
		"status" : 1
	},
	{
		"idx" : 757,
		"title" : "오막회집",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/9vlNqHB2fewS",
		"status" : 1
	},
	{
		"idx" : 758,
		"title" : "나에게오는길",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/qC0JqUYyBRpZ",
		"status" : 1
	},
	{
		"idx" : 759,
		"title" : "낙원의소바",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/kIQQiAevCNmR",
		"status" : 1
	},
	{
		"idx" : 760,
		"title" : "락구정",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/czUTF2uHds",
		"status" : 1
	},
	{
		"idx" : 761,
		"title" : "호랑이면",
		"score" : "3.5",
		"region" : "관악구",
		"url" : "https://www.mangoplate.com/restaurants/z8gYJaCT1wkU",
		"status" : 1
	},
	{
		"idx" : 762,
		"title" : "진영면옥",
		"score" : "4.3",
		"region" : "금천구",
		"url" : "https://www.mangoplate.com/restaurants/Yf4ZnjI3zUw8",
		"status" : 1
	},
	{
		"idx" : 763,
		"title" : "여신족발",
		"score" : "4.3",
		"region" : "금천구",
		"url" : "https://www.mangoplate.com/restaurants/BGIEFmOCX3",
		"status" : 1
	},
	{
		"idx" : 764,
		"title" : "김사부샤브샤브 무한리필",
		"score" : "4.2",
		"region" : "금천구",
		"url" : "https://www.mangoplate.com/restaurants/Pihxs9arIHF1",
		"status" : 1
	},
	{
		"idx" : 765,
		"title" : "호세가",
		"score" : "4.2",
		"region" : "금천구",
		"url" : "https://www.mangoplate.com/restaurants/03F6o0Z0GV-3",
		"status" : 1
	},
	{
		"idx" : 766,
		"title" : "만두라",
		"score" : "4.1",
		"region" : "금천구",
		"url" : "https://www.mangoplate.com/restaurants/T56ii3aPmLs9",
		"status" : 1
	},
	{
		"idx" : 767,
		"title" : "금천칼국수",
		"score" : "4.1",
		"region" : "금천구",
		"url" : "https://www.mangoplate.com/restaurants/4sH5lGrqcl",
		"status" : 1
	},
	{
		"idx" : 768,
		"title" : "가산물갈비&백년불고기",
		"score" : "4.1",
		"region" : "금천구",
		"url" : "https://www.mangoplate.com/restaurants/v3NI2NUSb0y4",
		"status" : 1
	},
	{
		"idx" : 769,
		"title" : "세라즈피자펍",
		"score" : "3.9",
		"region" : "금천구",
		"url" : "https://www.mangoplate.com/restaurants/3klrsBgK1uxy",
		"status" : 1
	},
	{
		"idx" : 770,
		"title" : "인크커피",
		"score" : "3.7",
		"region" : "금천구",
		"url" : "https://www.mangoplate.com/restaurants/pjJCAz7s_OuC",
		"status" : 1
	},
	{
		"idx" : 771,
		"title" : "춘천옥",
		"score" : "3.5",
		"region" : "금천구",
		"url" : "https://www.mangoplate.com/restaurants/a8yeGPQtrF",
		"status" : 1
	},
	{
		"idx" : 772,
		"title" : "떡볶이랑걸레만두랑",
		"score" : "3.4",
		"region" : "금천구",
		"url" : "https://www.mangoplate.com/restaurants/BCcVCT6xLO",
		"status" : 1
	},
	{
		"idx" : 773,
		"title" : "동흥관",
		"score" : "3.3",
		"region" : "금천구",
		"url" : "https://www.mangoplate.com/restaurants/eW39AJFhMT",
		"status" : 1
	},
	{
		"idx" : 774,
		"title" : "동신면가",
		"score" : "3.9",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/wB8mzbTzkv",
		"status" : 1
	},
	{
		"idx" : 775,
		"title" : "샘밭막국수",
		"score" : "3.9",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/w0oGI4fH_W",
		"status" : 1
	},
	{
		"idx" : 776,
		"title" : "소울버킷",
		"score" : "3.9",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/NvJpAklb8jXQ",
		"status" : 1
	},
	{
		"idx" : 777,
		"title" : "백화네부엌",
		"score" : "3.9",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/871YkTM6nEFU",
		"status" : 1
	},
	{
		"idx" : 778,
		"title" : "스시카이",
		"score" : "3.8",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/iYN8mCl6Vqoz",
		"status" : 1
	},
	{
		"idx" : 779,
		"title" : "스시진수",
		"score" : "3.8",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/kQ9fklyrBhDy",
		"status" : 1
	},
	{
		"idx" : 780,
		"title" : "세광양대창",
		"score" : "3.8",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/HI7AU-t3qY2n",
		"status" : 1
	},
	{
		"idx" : 781,
		"title" : "탐라도야지",
		"score" : "3.8",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/ZlnDgOHEvd",
		"status" : 1
	},
	{
		"idx" : 782,
		"title" : "광해즉석떡볶이",
		"score" : "3.8",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/-KJXSYgS2XE8",
		"status" : 1
	},
	{
		"idx" : 783,
		"title" : "황금콩밭",
		"score" : "3.8",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/Q-CHdwbm18AL",
		"status" : 1
	},
	{
		"idx" : 784,
		"title" : "마라공방",
		"score" : "3.8",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/drQeQqUQxV17",
		"status" : 1
	},
	{
		"idx" : 785,
		"title" : "교대이층집",
		"score" : "3.7",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/U0s5Dls5_8",
		"status" : 1
	},
	{
		"idx" : 786,
		"title" : "아이스시 스시사랑",
		"score" : "3.7",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/3BCgRxfVdlTU",
		"status" : 1
	},
	{
		"idx" : 787,
		"title" : "마음은콩밭에",
		"score" : "3.7",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/7lNGg7h5GL",
		"status" : 1
	},
	{
		"idx" : 788,
		"title" : "바스버거",
		"score" : "3.7",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/WPcQMJzfgNoj",
		"status" : 1
	},
	{
		"idx" : 789,
		"title" : "항방양육관",
		"score" : "3.6",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/Utz0dBk1bi",
		"status" : 1
	},
	{
		"idx" : 790,
		"title" : "그림나베",
		"score" : "3.6",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/sOtV01IQuy09",
		"status" : 1
	},
	{
		"idx" : 791,
		"title" : "친친마라탕",
		"score" : "3.6",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/ykSMGQAA-Ti-",
		"status" : 1
	},
	{
		"idx" : 792,
		"title" : "이여곰탕",
		"score" : "3.6",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/3WgFxkOm0gDs",
		"status" : 1
	},
	{
		"idx" : 793,
		"title" : "명동곰돌이",
		"score" : "3.6",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/EYuaox-vzO",
		"status" : 1
	},
	{
		"idx" : 794,
		"title" : "교대갈비집",
		"score" : "3.6",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/S3FKjIUNleYQ",
		"status" : 1
	},
	{
		"idx" : 795,
		"title" : "카츠공방",
		"score" : "3.6",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/XTzaeqtdvKso",
		"status" : 1
	},
	{
		"idx" : 796,
		"title" : "타이반쩜",
		"score" : "3.5",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/WJq3gH1xVGGN",
		"status" : 1
	},
	{
		"idx" : 797,
		"title" : "어반아이트",
		"score" : "3.4",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/9QvgkbpXiP",
		"status" : 1
	},
	{
		"idx" : 798,
		"title" : "창화당",
		"score" : "3.4",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/J0znTFvyuGyJ",
		"status" : 1
	},
	{
		"idx" : 799,
		"title" : "호랑이초밥",
		"score" : "3.4",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/qGbHzkRHY18j",
		"status" : 1
	},
	{
		"idx" : 800,
		"title" : "삼산회관",
		"score" : "3.3",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/GUFYXg2sLi9N",
		"status" : 1
	},
	{
		"idx" : 801,
		"title" : "교대곱창",
		"score" : "3.3",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/hVHlaGskpD",
		"status" : 1
	},
	{
		"idx" : 802,
		"title" : "갈릭앤페퍼",
		"score" : "3.3",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/CH7wvoUZ2D",
		"status" : 1
	},
	{
		"idx" : 803,
		"title" : "교대평상집",
		"score" : "3.2",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/wsbRSRPMQRdz",
		"status" : 1
	},
	{
		"idx" : 804,
		"title" : "뽕사부",
		"score" : "3.2",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/Yiwzv9ZLCXpV",
		"status" : 1
	},
	{
		"idx" : 805,
		"title" : "챱챱케이크",
		"score" : "2.8",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/xDft1Az2uKY5",
		"status" : 1
	},
	{
		"idx" : 806,
		"title" : "서관면옥",
		"score" : "4.6",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/0kuRscmhbREW",
		"status" : 1
	},
	{
		"idx" : 807,
		"title" : "설눈",
		"score" : "4.5",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/iXjQqcw9rdi4",
		"status" : 1
	},
	{
		"idx" : 808,
		"title" : "스시 윤슬",
		"score" : "4.5",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/liF5vKerK4Rj",
		"status" : 1
	},
	{
		"idx" : 809,
		"title" : "하레",
		"score" : "4.4",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/1Ikh-sUkDV",
		"status" : 1
	},
	{
		"idx" : 810,
		"title" : "제주성산포바당",
		"score" : "4.4",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/1Y7Xo0PrEgSB",
		"status" : 1
	},
	{
		"idx" : 811,
		"title" : "앙띠크",
		"score" : "4.4",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/ANFRhzAJWPhf",
		"status" : 1
	},
	{
		"idx" : 812,
		"title" : "3대삼계장인",
		"score" : "4.4",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/i2DHGjSOYR9O",
		"status" : 1
	},
	{
		"idx" : 813,
		"title" : "산도",
		"score" : "4.3",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/0RROU5RXxNPC",
		"status" : 1
	},
	{
		"idx" : 814,
		"title" : "한성양꼬치",
		"score" : "4.3",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/sQRORYMhuBiO",
		"status" : 1
	},
	{
		"idx" : 815,
		"title" : "마라청춘마라탕",
		"score" : "4.3",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/kvEaBgiuCYC2",
		"status" : 1
	},
	{
		"idx" : 816,
		"title" : "스시소라",
		"score" : "4.1",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/GPLI6QrrJmmO",
		"status" : 1
	},
	{
		"idx" : 817,
		"title" : "고스트요거트",
		"score" : "4.1",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/CNdRE90wfWxd",
		"status" : 1
	},
	{
		"idx" : 818,
		"title" : "미니말레 커피뢰스터",
		"score" : "4.1",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/Add50ZjI1dn-",
		"status" : 1
	},
	{
		"idx" : 819,
		"title" : "가츠오",
		"score" : "4.0",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/KgJm1LpfHl6L",
		"status" : 1
	},
	{
		"idx" : 820,
		"title" : "쿤쏨차이",
		"score" : "4.0",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/ef28wYY53TfM",
		"status" : 1
	},
	{
		"idx" : 821,
		"title" : "공간21",
		"score" : "4.0",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/rzJrPxF7LpuJ",
		"status" : 1
	},
	{
		"idx" : 822,
		"title" : "서초면옥",
		"score" : "4.0",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/Tvr9CwDGB5",
		"status" : 1
	},
	{
		"idx" : 823,
		"title" : "이심전심 언양불고기",
		"score" : "4.0",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/QmL1M7zWUe",
		"status" : 1
	},
	{
		"idx" : 824,
		"title" : "믿을신",
		"score" : "4.0",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/Qfyb3EYhX9Ku",
		"status" : 1
	},
	{
		"idx" : 825,
		"title" : "어스마카롱",
		"score" : "4.0",
		"region" : "교대/서초",
		"url" : "https://www.mangoplate.com/restaurants/_9YX_qZFBKPx",
		"status" : 1
	},
	{
		"idx" : 826,
		"title" : "비밀시그니쳐",
		"score" : "3.3",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/8bqAUQb96Z5S",
		"status" : 1
	},
	{
		"idx" : 827,
		"title" : "맛찬들왕소금구이",
		"score" : "3.3",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/hi5SXCW12-L_",
		"status" : 1
	},
	{
		"idx" : 828,
		"title" : "또치분식",
		"score" : "3.3",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/T6x2o6CJi-",
		"status" : 1
	},
	{
		"idx" : 829,
		"title" : "메이비",
		"score" : "3.2",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/l-5w00C1l7",
		"status" : 1
	},
	{
		"idx" : 830,
		"title" : "이춘복참치",
		"score" : "3.2",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/4EoW0JyMkt",
		"status" : 1
	},
	{
		"idx" : 831,
		"title" : "말뚝곱창",
		"score" : "3.2",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/BUwt6E9g7V",
		"status" : 1
	},
	{
		"idx" : 832,
		"title" : "라그릴리아",
		"score" : "3.2",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/aicYlrUNGvXh",
		"status" : 1
	},
	{
		"idx" : 833,
		"title" : "신승반점",
		"score" : "3.2",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/MNDXTu3itDMQ",
		"status" : 1
	},
	{
		"idx" : 834,
		"title" : "백채 김치찌개",
		"score" : "3.2",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/5DeEbQo5yAeh",
		"status" : 1
	},
	{
		"idx" : 835,
		"title" : "삿뽀로",
		"score" : "3.1",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/oh16BeTDDZEN",
		"status" : 1
	},
	{
		"idx" : 836,
		"title" : "후와후와",
		"score" : "3.0",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/XXMoayc6RPVP",
		"status" : 1
	},
	{
		"idx" : 837,
		"title" : "백미당",
		"score" : "3.0",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/vE4xpG7ENyuU",
		"status" : 1
	},
	{
		"idx" : 838,
		"title" : "퍼틴",
		"score" : "2.9",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/NaT5moVFBFca",
		"status" : 1
	},
	{
		"idx" : 839,
		"title" : "라꾸긴",
		"score" : "4.3",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/1cKCuayTDdSb",
		"status" : 1
	},
	{
		"idx" : 840,
		"title" : "등포",
		"score" : "4.3",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/-8fXUyjxBBvC",
		"status" : 1
	},
	{
		"idx" : 841,
		"title" : "월래순교자관",
		"score" : "4.2",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/0fVczJphgFWa",
		"status" : 1
	},
	{
		"idx" : 842,
		"title" : "낭만부대찌개",
		"score" : "4.0",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/ZMXbPplox6",
		"status" : 1
	},
	{
		"idx" : 843,
		"title" : "춘자싸롱",
		"score" : "4.0",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/KXlSndzlh8",
		"status" : 1
	},
	{
		"idx" : 844,
		"title" : "엉베흐",
		"score" : "4.0",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/GUcU2CdBvkn1",
		"status" : 1
	},
	{
		"idx" : 845,
		"title" : "교레츠라멘",
		"score" : "4.0",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/cKdztiu9FfTD",
		"status" : 1
	},
	{
		"idx" : 846,
		"title" : "정겨운오뎅집",
		"score" : "4.0",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/jfzvikOySF",
		"status" : 1
	},
	{
		"idx" : 847,
		"title" : "신도림참족발",
		"score" : "3.9",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/N0gzPzNH0Zoj",
		"status" : 1
	},
	{
		"idx" : 848,
		"title" : "서울안심축산정육식당",
		"score" : "3.9",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/Do1fCz19Vg",
		"status" : 1
	},
	{
		"idx" : 849,
		"title" : "우월소곱창",
		"score" : "3.9",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/M_AvaDqUp4To",
		"status" : 1
	},
	{
		"idx" : 850,
		"title" : "강촌숯불닭갈비",
		"score" : "3.8",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/3RlZYRoqrx",
		"status" : 1
	},
	{
		"idx" : 851,
		"title" : "이스트바이게이트",
		"score" : "3.8",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/1aqNyjDPqXAt",
		"status" : 1
	},
	{
		"idx" : 852,
		"title" : "바르미 샤브샤브",
		"score" : "3.8",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/o-NAFIbQe6W3",
		"status" : 1
	},
	{
		"idx" : 853,
		"title" : "평양냉면",
		"score" : "3.7",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/ZWOXk2Ye9o",
		"status" : 1
	},
	{
		"idx" : 854,
		"title" : "신도림 이도식당",
		"score" : "3.7",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/HdqIvW7BT6XT",
		"status" : 1
	},
	{
		"idx" : 855,
		"title" : "라마노피자",
		"score" : "3.6",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/bDGH8e7E62-T",
		"status" : 1
	},
	{
		"idx" : 856,
		"title" : "밀리",
		"score" : "3.6",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/20pQpgpi9fss",
		"status" : 1
	},
	{
		"idx" : 857,
		"title" : "오목집",
		"score" : "3.6",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/gwkXPkvROBO-",
		"status" : 1
	},
	{
		"idx" : 858,
		"title" : "빈브라더스",
		"score" : "3.4",
		"region" : "구로구",
		"url" : "https://www.mangoplate.com/restaurants/v7lUz7MziM",
		"status" : 1
	},
	{
		"idx" : 859,
		"title" : "엉짱윤치킨",
		"score" : "3.5",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/L9lQ9kpiVtMx",
		"status" : 1
	},
	{
		"idx" : 860,
		"title" : "스시노미찌",
		"score" : "3.4",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/eLQUJ_0s7Y",
		"status" : 1
	},
	{
		"idx" : 861,
		"title" : "시민막국수 숯불닭갈비",
		"score" : "3.4",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/LUBzObp1w3Qk",
		"status" : 1
	},
	{
		"idx" : 862,
		"title" : "가쯔레쯔",
		"score" : "3.4",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/vq014uOrGh",
		"status" : 1
	},
	{
		"idx" : 863,
		"title" : "마키나리",
		"score" : "3.3",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/v6mSflzbelFz",
		"status" : 1
	},
	{
		"idx" : 864,
		"title" : "빕스",
		"score" : "3.3",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/SVZbRJ92SQMQ",
		"status" : 1
	},
	{
		"idx" : 865,
		"title" : "은행골",
		"score" : "3.2",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/smx8JdC5Woln",
		"status" : 1
	},
	{
		"idx" : 866,
		"title" : "스쿨푸드",
		"score" : "3.2",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/KqOHBmSjqh",
		"status" : 1
	},
	{
		"idx" : 867,
		"title" : "토다이U",
		"score" : "3.0",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/z2xyMvvMbH",
		"status" : 1
	},
	{
		"idx" : 868,
		"title" : "서가앤쿡",
		"score" : "3.0",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/zrHNzBq2D3",
		"status" : 1
	},
	{
		"idx" : 869,
		"title" : "신야텐야",
		"score" : "2.9",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/BNovNm7pBDZ0",
		"status" : 1
	},
	{
		"idx" : 870,
		"title" : "팔각도",
		"score" : "3.8",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/ny7ksCBq2bG5",
		"status" : 1
	},
	{
		"idx" : 871,
		"title" : "애틱인서울하우스",
		"score" : "3.8",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/nh_lH8JRvFwo",
		"status" : 1
	},
	{
		"idx" : 872,
		"title" : "한스",
		"score" : "3.8",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/_548OAOl_n",
		"status" : 1
	},
	{
		"idx" : 873,
		"title" : "라고파스타",
		"score" : "3.7",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/N3Lz7vPdMw",
		"status" : 1
	},
	{
		"idx" : 874,
		"title" : "푸오꼬",
		"score" : "3.7",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/1QesQYIBsK",
		"status" : 1
	},
	{
		"idx" : 875,
		"title" : "젠틀한식탁",
		"score" : "3.7",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/qflZw8l-0b8x",
		"status" : 1
	},
	{
		"idx" : 876,
		"title" : "쿠마카세",
		"score" : "3.7",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/FGSz2qNBuu",
		"status" : 1
	},
	{
		"idx" : 877,
		"title" : "아리네",
		"score" : "3.7",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/nuD9izKNd2zq",
		"status" : 1
	},
	{
		"idx" : 878,
		"title" : "레몬버베나",
		"score" : "3.7",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/5c2chJy4JYgk",
		"status" : 1
	},
	{
		"idx" : 879,
		"title" : "닥터로빈",
		"score" : "3.6",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/xVrKXt1KVA",
		"status" : 1
	},
	{
		"idx" : 880,
		"title" : "엉털네숯불꼼장어",
		"score" : "3.6",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/1I7OD5NckN",
		"status" : 1
	},
	{
		"idx" : 881,
		"title" : "아모르버터",
		"score" : "3.6",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/GkhTgVYX5P_o",
		"status" : 1
	},
	{
		"idx" : 882,
		"title" : "쿠마카레",
		"score" : "3.6",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/WgPdJCCoR9vn",
		"status" : 1
	},
	{
		"idx" : 883,
		"title" : "카페 제하",
		"score" : "3.6",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/FPCe68u3P4Vy",
		"status" : 1
	},
	{
		"idx" : 884,
		"title" : "커피별녹색잔",
		"score" : "3.6",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/e8NNI3-WpFea",
		"status" : 1
	},
	{
		"idx" : 885,
		"title" : "댓짱돈까스",
		"score" : "3.6",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/TSROgRGisK",
		"status" : 1
	},
	{
		"idx" : 886,
		"title" : "에프스토리",
		"score" : "3.5",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/ltnEjOZlOH",
		"status" : 1
	},
	{
		"idx" : 887,
		"title" : "목동버거",
		"score" : "3.5",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/hqCgta3qpAZK",
		"status" : 1
	},
	{
		"idx" : 888,
		"title" : "살구나무집칼국수",
		"score" : "3.5",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/sD7fze3iCt",
		"status" : 1
	},
	{
		"idx" : 889,
		"title" : "평미가",
		"score" : "3.5",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/Eis5YkWDyZ",
		"status" : 1
	},
	{
		"idx" : 890,
		"title" : "강릉스낵",
		"score" : "4.3",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/Dp-F_2o17eDB",
		"status" : 1
	},
	{
		"idx" : 891,
		"title" : "목동해물",
		"score" : "4.3",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/Pv4ElQQIZK",
		"status" : 1
	},
	{
		"idx" : 892,
		"title" : "히노야마",
		"score" : "4.2",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/iuwHvXZjVeGr",
		"status" : 1
	},
	{
		"idx" : 893,
		"title" : "반쌥",
		"score" : "4.1",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/7y0jpyy-3N1A",
		"status" : 1
	},
	{
		"idx" : 894,
		"title" : "우직서울",
		"score" : "4.1",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/XlgM9X_hqFU-",
		"status" : 1
	},
	{
		"idx" : 895,
		"title" : "미시락칼국수",
		"score" : "4.1",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/D49sRLtT_W",
		"status" : 1
	},
	{
		"idx" : 896,
		"title" : "밥초",
		"score" : "4.1",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/6XFfrdg-h7b-",
		"status" : 1
	},
	{
		"idx" : 897,
		"title" : "팔방교자",
		"score" : "4.0",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/scqcxV7Y69eb",
		"status" : 1
	},
	{
		"idx" : 898,
		"title" : "홍마방",
		"score" : "4.0",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/K3DFgepmBg6r",
		"status" : 1
	},
	{
		"idx" : 899,
		"title" : "이키이키",
		"score" : "4.0",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/jdmRhxsomaDA",
		"status" : 1
	},
	{
		"idx" : 900,
		"title" : "가랑삼계탕",
		"score" : "4.0",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/UzWhwg-E_D",
		"status" : 1
	},
	{
		"idx" : 901,
		"title" : "일미락",
		"score" : "3.9",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/8IMM7P08_F",
		"status" : 1
	},
	{
		"idx" : 902,
		"title" : "카멜리온",
		"score" : "3.9",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/zw8Y-XKD_I5M",
		"status" : 1
	},
	{
		"idx" : 903,
		"title" : "금성수제돈까스",
		"score" : "3.9",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/A4JzUBKB2byZ",
		"status" : 1
	},
	{
		"idx" : 904,
		"title" : "진미집",
		"score" : "3.9",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/N1lRmm1aHT7K",
		"status" : 1
	},
	{
		"idx" : 905,
		"title" : "오봉집",
		"score" : "3.9",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/qqn7JKwtYDEL",
		"status" : 1
	},
	{
		"idx" : 906,
		"title" : "나이스크림",
		"score" : "3.9",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/m-w-LKW4g5Ln",
		"status" : 1
	},
	{
		"idx" : 907,
		"title" : "오목집",
		"score" : "3.8",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/wWfxlwULHl",
		"status" : 1
	},
	{
		"idx" : 908,
		"title" : "파티세리소나",
		"score" : "3.8",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/UTcq3Hi0I3F1",
		"status" : 1
	},
	{
		"idx" : 909,
		"title" : "락희안",
		"score" : "3.8",
		"region" : "목동/양천",
		"url" : "https://www.mangoplate.com/restaurants/UR1XUbReU3wj",
		"status" : 1
	},
	{
		"idx" : 910,
		"title" : "심야식당켬",
		"score" : "3.7",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/X0p17hO-3in_",
		"status" : 1
	},
	{
		"idx" : 911,
		"title" : "옛날한우곱창전문",
		"score" : "3.7",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/UeMLbg6MrN",
		"status" : 1
	},
	{
		"idx" : 912,
		"title" : "루브레드",
		"score" : "3.7",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/LEwAksVTuZwB",
		"status" : 1
	},
	{
		"idx" : 913,
		"title" : "김종용누룽지통닭",
		"score" : "3.7",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/gaDU-uzJjB2P",
		"status" : 1
	},
	{
		"idx" : 914,
		"title" : "등촌최월선칼국수",
		"score" : "3.6",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/ORiGuyC8Gn",
		"status" : 1
	},
	{
		"idx" : 915,
		"title" : "유림",
		"score" : "3.6",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/-IPS7rjEmj",
		"status" : 1
	},
	{
		"idx" : 916,
		"title" : "안영자면옥",
		"score" : "3.6",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/7wDa2w17Xt4b",
		"status" : 1
	},
	{
		"idx" : 917,
		"title" : "닥터로빈",
		"score" : "3.6",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/_tgAYehd_t",
		"status" : 1
	},
	{
		"idx" : 918,
		"title" : "랑 월",
		"score" : "3.6",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/KqoyCW483zDy",
		"status" : 1
	},
	{
		"idx" : 919,
		"title" : "스몰스파이시올리브",
		"score" : "3.6",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/qhyShwdlCjzX",
		"status" : 1
	},
	{
		"idx" : 920,
		"title" : "강릉엄지네꼬막집",
		"score" : "3.6",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/c7vHUvDdLSQE",
		"status" : 1
	},
	{
		"idx" : 921,
		"title" : "냐항바바바",
		"score" : "3.6",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/BX6mUwKU00hi",
		"status" : 1
	},
	{
		"idx" : 922,
		"title" : "브런치팩토리",
		"score" : "3.6",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/f6flpFYg2EsT",
		"status" : 1
	},
	{
		"idx" : 923,
		"title" : "탄탄면공방",
		"score" : "3.6",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/JwwFHWNp4cER",
		"status" : 1
	},
	{
		"idx" : 924,
		"title" : "긴꼬리초밥",
		"score" : "3.6",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/vBlLjMTERpve",
		"status" : 1
	},
	{
		"idx" : 925,
		"title" : "소바트럭",
		"score" : "3.5",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/iZs55Z5JnDrN",
		"status" : 1
	},
	{
		"idx" : 926,
		"title" : "똑순이막국수",
		"score" : "3.5",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/fhidOJQDp6",
		"status" : 1
	},
	{
		"idx" : 927,
		"title" : "카페우드진",
		"score" : "3.5",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/fR_Mns0FKRU0",
		"status" : 1
	},
	{
		"idx" : 928,
		"title" : "목동분식",
		"score" : "3.5",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/fgWFfSJfB0",
		"status" : 1
	},
	{
		"idx" : 929,
		"title" : "광화문살롱",
		"score" : "3.5",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/Fuon_Whz871b",
		"status" : 1
	},
	{
		"idx" : 930,
		"title" : "타이반쩜",
		"score" : "4.1",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/BWlykCA0YZdx",
		"status" : 1
	},
	{
		"idx" : 931,
		"title" : "란콰이펑누들",
		"score" : "4.1",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/H_QNnqFhGXXE",
		"status" : 1
	},
	{
		"idx" : 932,
		"title" : "사미식당",
		"score" : "4.1",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/sQ_m26yQigax",
		"status" : 1
	},
	{
		"idx" : 933,
		"title" : "우아하계",
		"score" : "4.1",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/_WUn6-9hKVc-",
		"status" : 1
	},
	{
		"idx" : 934,
		"title" : "바삭하게",
		"score" : "4.1",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/pFkzBjoFhxM6",
		"status" : 1
	},
	{
		"idx" : 935,
		"title" : "코끼리탭룸",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/MwuyMzGGW9Y4",
		"status" : 1
	},
	{
		"idx" : 936,
		"title" : "헝그리부처",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/iV2E1hyYlWj3",
		"status" : 1
	},
	{
		"idx" : 937,
		"title" : "배진수어시장",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/ISXhAWEo1tJJ",
		"status" : 1
	},
	{
		"idx" : 938,
		"title" : "오지오커피",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/56lLSEWZjHzr",
		"status" : 1
	},
	{
		"idx" : 939,
		"title" : "스즈란테이",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/Prw81RG2pXlP",
		"status" : 1
	},
	{
		"idx" : 940,
		"title" : "잔잔하게",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/_WfnJQRQUV1M",
		"status" : 1
	},
	{
		"idx" : 941,
		"title" : "광주똑순이",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/BOD-qlKuAf",
		"status" : 1
	},
	{
		"idx" : 942,
		"title" : "충북식당",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/fWrJcvMIykcQ",
		"status" : 1
	},
	{
		"idx" : 943,
		"title" : "고양이똥3",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/9VXY3W9iqunu",
		"status" : 1
	},
	{
		"idx" : 944,
		"title" : "르와조",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/eySvZLhQKSZi",
		"status" : 1
	},
	{
		"idx" : 945,
		"title" : "저스트텐동",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/9xJWvy2P7jz7",
		"status" : 1
	},
	{
		"idx" : 946,
		"title" : "와카츠",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/HtJYU3lIn2Ix",
		"status" : 1
	},
	{
		"idx" : 947,
		"title" : "데판야끼다케시",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/gY__D-JtKtc3",
		"status" : 1
	},
	{
		"idx" : 948,
		"title" : "슬로우캘리",
		"score" : "4.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/eRKUC3q5ty9P",
		"status" : 1
	},
	{
		"idx" : 949,
		"title" : "나오키",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/UEfXcegzKVt1",
		"status" : 1
	},
	{
		"idx" : 950,
		"title" : "바코",
		"score" : "4.6",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/zzulPTWCNorK",
		"status" : 1
	},
	{
		"idx" : 951,
		"title" : "자이온",
		"score" : "4.4",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/tVD0FPJEe0q9",
		"status" : 1
	},
	{
		"idx" : 952,
		"title" : "조연탄",
		"score" : "4.3",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/9xGdpGAUx-",
		"status" : 1
	},
	{
		"idx" : 953,
		"title" : "금고깃집",
		"score" : "4.3",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/POFrRq_mT1SJ",
		"status" : 1
	},
	{
		"idx" : 954,
		"title" : "영양족발순대국",
		"score" : "4.3",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/9qHLgnJtje",
		"status" : 1
	},
	{
		"idx" : 955,
		"title" : "산청숯불가든",
		"score" : "4.3",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/qYVn1eeRo9tY",
		"status" : 1
	},
	{
		"idx" : 956,
		"title" : "원조나주곰탕",
		"score" : "4.3",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/4Vzg7olJy3",
		"status" : 1
	},
	{
		"idx" : 957,
		"title" : "하양옥",
		"score" : "4.3",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/u1IAbXZAODh4",
		"status" : 1
	},
	{
		"idx" : 958,
		"title" : "마초갈비",
		"score" : "4.3",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/KrR-KeedDG5G",
		"status" : 1
	},
	{
		"idx" : 959,
		"title" : "희희잇",
		"score" : "4.3",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/OnPRCVCMto4L",
		"status" : 1
	},
	{
		"idx" : 960,
		"title" : "마부자생삼겹살",
		"score" : "4.2",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/2LbtRZVu0EJT",
		"status" : 1
	},
	{
		"idx" : 961,
		"title" : "웜테이블",
		"score" : "4.2",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/HaBW5K2AMYM3",
		"status" : 1
	},
	{
		"idx" : 962,
		"title" : "사이공윤다이",
		"score" : "4.2",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/t2d7sl1n3mpq",
		"status" : 1
	},
	{
		"idx" : 963,
		"title" : "김치옥",
		"score" : "4.2",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/y42934PeaJu5",
		"status" : 1
	},
	{
		"idx" : 964,
		"title" : "헤리스헤이스",
		"score" : "4.2",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/UDGbMxnZ8iob",
		"status" : 1
	},
	{
		"idx" : 965,
		"title" : "강순자옛맛김치찌개",
		"score" : "4.2",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/NCTjU3Yv4Rr8",
		"status" : 1
	},
	{
		"idx" : 966,
		"title" : "떼헤브 (휴업중)",
		"score" : "4.1",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/jqMAPk9ZHOFL",
		"status" : 1
	},
	{
		"idx" : 967,
		"title" : "공간녹음",
		"score" : "4.1",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/sRvZru88ZTMf",
		"status" : 1
	},
	{
		"idx" : 968,
		"title" : "청기와타운",
		"score" : "4.1",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/mImhib7_Oke_",
		"status" : 1
	},
	{
		"idx" : 969,
		"title" : "Poke all day포케&샐러드",
		"score" : "4.1",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/6nHUPGHWkyHU",
		"status" : 1
	},
	{
		"idx" : 970,
		"title" : "능라도",
		"score" : "3.5",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/d2CGUm8SoZvi",
		"status" : 1
	},
	{
		"idx" : 971,
		"title" : "뚜스뚜스",
		"score" : "3.5",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/iRMvnyPMJTYW",
		"status" : 1
	},
	{
		"idx" : 972,
		"title" : "동양식당",
		"score" : "3.5",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/rgR1hjlo6dDN",
		"status" : 1
	},
	{
		"idx" : 973,
		"title" : "이름없는달밤",
		"score" : "3.5",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/vtlZBf_f5hoS",
		"status" : 1
	},
	{
		"idx" : 974,
		"title" : "서울미트볼",
		"score" : "3.5",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/JP4CbBFP3inL",
		"status" : 1
	},
	{
		"idx" : 975,
		"title" : "고성막국수",
		"score" : "3.4",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/HcLg6DXr_Z",
		"status" : 1
	},
	{
		"idx" : 976,
		"title" : "헤븐온탑",
		"score" : "3.4",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/WA2X2KQPl7eL",
		"status" : 1
	},
	{
		"idx" : 977,
		"title" : "꼼떼바베큐",
		"score" : "3.4",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/71kzAKMoxLAH",
		"status" : 1
	},
	{
		"idx" : 978,
		"title" : "경아식당",
		"score" : "3.4",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/f7GUzbQTsCMA",
		"status" : 1
	},
	{
		"idx" : 979,
		"title" : "파파노다이닝",
		"score" : "3.4",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/IijQuz8aYWCi",
		"status" : 1
	},
	{
		"idx" : 980,
		"title" : "타이투고",
		"score" : "3.4",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/uwJEM0q5BXU8",
		"status" : 1
	},
	{
		"idx" : 981,
		"title" : "동굴",
		"score" : "3.4",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/WvSlE3tu_D9a",
		"status" : 1
	},
	{
		"idx" : 982,
		"title" : "인라이크",
		"score" : "3.4",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/MUaLmazBLxRC",
		"status" : 1
	},
	{
		"idx" : 983,
		"title" : "드렁킨타이",
		"score" : "3.4",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/3mZXeW_lXDiR",
		"status" : 1
	},
	{
		"idx" : 984,
		"title" : "OBPC",
		"score" : "3.4",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/5HrumCmg_sK8",
		"status" : 1
	},
	{
		"idx" : 985,
		"title" : "맛찬들왕소금구이",
		"score" : "3.3",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/eWrtJhGvRY",
		"status" : 1
	},
	{
		"idx" : 986,
		"title" : "백소정",
		"score" : "3.3",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/-U3CsaOrXXOT",
		"status" : 1
	},
	{
		"idx" : 987,
		"title" : "공항칼국수",
		"score" : "3.2",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/9N04QVnS7u",
		"status" : 1
	},
	{
		"idx" : 988,
		"title" : "토끼정",
		"score" : "3.2",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/EQDRfmhizXRU",
		"status" : 1
	},
	{
		"idx" : 989,
		"title" : "대림국수",
		"score" : "3.0",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/pFv5x61TAAmY",
		"status" : 1
	},
	{
		"idx" : 990,
		"title" : "스시사라",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/SgHnz6uasRY_",
		"status" : 1
	},
	{
		"idx" : 991,
		"title" : "발산삼계탕",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/MX7DwkJPRH",
		"status" : 1
	},
	{
		"idx" : 992,
		"title" : "송쭈집",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/vFIGPLy9dlIi",
		"status" : 1
	},
	{
		"idx" : 993,
		"title" : "마므레 크로와상",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/Gmc2DxOxBt_3",
		"status" : 1
	},
	{
		"idx" : 994,
		"title" : "고드니",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/ooqk1c6WvFK4",
		"status" : 1
	},
	{
		"idx" : 995,
		"title" : "후라토식당",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/IsYRmtkZ6ijJ",
		"status" : 1
	},
	{
		"idx" : 996,
		"title" : "오우야 에스프레소바",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/G9QMXtnGt6NH",
		"status" : 1
	},
	{
		"idx" : 997,
		"title" : "맹순이꽃게아구찜",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/t3mUdFRHroAE",
		"status" : 1
	},
	{
		"idx" : 998,
		"title" : "밀화당",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/EW0UOgz1nWEO",
		"status" : 1
	},
	{
		"idx" : 999,
		"title" : "쏭타이치앙마이",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/mHOUNmGvAA-B",
		"status" : 1
	},
	{
		"idx" : 1000,
		"title" : "카페 티에리",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/pW_g2lMJ0hSm",
		"status" : 1
	},
	{
		"idx" : 1001,
		"title" : "리제르바",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/tQPbUsDsd934",
		"status" : 1
	},
	{
		"idx" : 1002,
		"title" : "연희김밥",
		"score" : "3.9",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/gV7CWiGaezVZ",
		"status" : 1
	},
	{
		"idx" : 1003,
		"title" : "고양이똥",
		"score" : "3.8",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/goeSeWVKZp",
		"status" : 1
	},
	{
		"idx" : 1004,
		"title" : "타르데마",
		"score" : "3.8",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/rMfTJTSKPRmf",
		"status" : 1
	},
	{
		"idx" : 1005,
		"title" : "옥소반",
		"score" : "3.8",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/JkaHHwhts7VZ",
		"status" : 1
	},
	{
		"idx" : 1006,
		"title" : "어나더사이드",
		"score" : "3.8",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/1ZYo8DghkwD6",
		"status" : 1
	},
	{
		"idx" : 1007,
		"title" : "바스버거",
		"score" : "3.8",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/TuRNSYEFfc-F",
		"status" : 1
	},
	{
		"idx" : 1008,
		"title" : "속초그바람에",
		"score" : "3.8",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/l9_JpEsK9ryW",
		"status" : 1
	},
	{
		"idx" : 1009,
		"title" : "더블랙",
		"score" : "3.7",
		"region" : "등촌/강서",
		"url" : "https://www.mangoplate.com/restaurants/pwXClztNzEna",
		"status" : 1
	},
	{
		"idx" : 1010,
		"title" : "파오파오",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/qJU5J5hrxX",
		"status" : 1
	},
	{
		"idx" : 1011,
		"title" : "신양로스터스",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/XV5xkvKoJFIi",
		"status" : 1
	},
	{
		"idx" : 1012,
		"title" : "송계옥",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/MQH6EBR6h8vQ",
		"status" : 1
	},
	{
		"idx" : 1013,
		"title" : "옥기린",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/jKAVOQNYodVy",
		"status" : 1
	},
	{
		"idx" : 1014,
		"title" : "유원설렁탕",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/K3pW4r43G8",
		"status" : 1
	},
	{
		"idx" : 1015,
		"title" : "육화식당",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/wfpZhXSq5J2l",
		"status" : 1
	},
	{
		"idx" : 1016,
		"title" : "냠냠물고기",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/OGuHCKX5zJaB",
		"status" : 1
	},
	{
		"idx" : 1017,
		"title" : "송파감자국",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/ehu_l-tXKl",
		"status" : 1
	},
	{
		"idx" : 1018,
		"title" : "동락",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/sBuBK3Tq5vbd",
		"status" : 1
	},
	{
		"idx" : 1019,
		"title" : "브로버거",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/YRyBl6OV5ay8",
		"status" : 1
	},
	{
		"idx" : 1020,
		"title" : "퍼햅스",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/98ZiGjQiHSZ1",
		"status" : 1
	},
	{
		"idx" : 1021,
		"title" : "코끼리 the salad cafe",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/E0GFxKj0qQMg",
		"status" : 1
	},
	{
		"idx" : 1022,
		"title" : "라미옥",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/W3-Jj9ZUJC2z",
		"status" : 1
	},
	{
		"idx" : 1023,
		"title" : "원조마포소금구이",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/G4XzlzNM1g",
		"status" : 1
	},
	{
		"idx" : 1024,
		"title" : "용기수산",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/0TK-6dYu_gjI",
		"status" : 1
	},
	{
		"idx" : 1025,
		"title" : "위커파크 웨스트",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/qnG72PPLUp8_",
		"status" : 1
	},
	{
		"idx" : 1026,
		"title" : "더빛남",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/1mOcrahO7SMh",
		"status" : 1
	},
	{
		"idx" : 1027,
		"title" : "한국계",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/__Ei0CCeDEZe",
		"status" : 1
	},
	{
		"idx" : 1028,
		"title" : "비바라비다 뮤지엄",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/kgkfPOd2fN28",
		"status" : 1
	},
	{
		"idx" : 1029,
		"title" : "탄포포",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/U1FwBlusG1db",
		"status" : 1
	},
	{
		"idx" : 1030,
		"title" : "도림 더 칸톤 테이블",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/H20ANdHUFr",
		"status" : 1
	},
	{
		"idx" : 1031,
		"title" : "해목",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/iHsjMVHB3Ahb",
		"status" : 1
	},
	{
		"idx" : 1032,
		"title" : "생생아구",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/qZydtN_dAjcL",
		"status" : 1
	},
	{
		"idx" : 1033,
		"title" : "서보",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/WjPrnNAHtngX",
		"status" : 1
	},
	{
		"idx" : 1034,
		"title" : "프롬헤라스",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/4E1ieVxEM2av",
		"status" : 1
	},
	{
		"idx" : 1035,
		"title" : "미강식당",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/DkCO6zKjdhe3",
		"status" : 1
	},
	{
		"idx" : 1036,
		"title" : "사사노하",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/LtdiLHvsZXJr",
		"status" : 1
	},
	{
		"idx" : 1037,
		"title" : "토마루해물칼국수",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/MPCs1uYDmwKY",
		"status" : 1
	},
	{
		"idx" : 1038,
		"title" : "스웨덴피크닉",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/T2QmXn4HJyXC",
		"status" : 1
	},
	{
		"idx" : 1039,
		"title" : "교차점",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/aej9GHfIzBd1",
		"status" : 1
	},
	{
		"idx" : 1040,
		"title" : "하얼빈양갈비엔양꼬치",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/z8YtSXYTcVCH",
		"status" : 1
	},
	{
		"idx" : 1041,
		"title" : "멘야하나비",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/sjYASRfuDxKr",
		"status" : 1
	},
	{
		"idx" : 1042,
		"title" : "옥돌현옥",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/4mrNxgid7sFL",
		"status" : 1
	},
	{
		"idx" : 1043,
		"title" : "봉피양",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/X2oyP4U6-a",
		"status" : 1
	},
	{
		"idx" : 1044,
		"title" : "오린지",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/Yuhf0XMAoC03",
		"status" : 1
	},
	{
		"idx" : 1045,
		"title" : "미엔아이",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/ztTTr81jaBm7",
		"status" : 1
	},
	{
		"idx" : 1046,
		"title" : "몽중헌",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/n4N6o-A4zE",
		"status" : 1
	},
	{
		"idx" : 1047,
		"title" : "야끼소바니주마루",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/Hps9zhInl69-",
		"status" : 1
	},
	{
		"idx" : 1048,
		"title" : "다운타우너",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/-jjalqkpiLPa",
		"status" : 1
	},
	{
		"idx" : 1049,
		"title" : "스시다원",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/yahqCovsJGoG",
		"status" : 1
	},
	{
		"idx" : 1050,
		"title" : "세이류",
		"score" : "4.8",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/R1Nzfed1UHqa",
		"status" : 1
	},
	{
		"idx" : 1051,
		"title" : "오향가",
		"score" : "4.6",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/IGPyzMELa6",
		"status" : 1
	},
	{
		"idx" : 1052,
		"title" : "돌마리유황오리",
		"score" : "4.6",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/eWI7PsA2Cw",
		"status" : 1
	},
	{
		"idx" : 1053,
		"title" : "레브어",
		"score" : "4.6",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/yy0VPDhV7mw7",
		"status" : 1
	},
	{
		"idx" : 1054,
		"title" : "밀각",
		"score" : "4.6",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/ZpE60fZcfqLK",
		"status" : 1
	},
	{
		"idx" : 1055,
		"title" : "칸다소바",
		"score" : "4.6",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/RxFRdDnCfIGs",
		"status" : 1
	},
	{
		"idx" : 1056,
		"title" : "엘리스리틀이태리",
		"score" : "4.5",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/vI2c9_tWVwoc",
		"status" : 1
	},
	{
		"idx" : 1057,
		"title" : "디저티스트",
		"score" : "4.5",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/KCcUzsJWALdw",
		"status" : 1
	},
	{
		"idx" : 1058,
		"title" : "차만다",
		"score" : "4.5",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/Br4jEi-pqzqz",
		"status" : 1
	},
	{
		"idx" : 1059,
		"title" : "그곁",
		"score" : "4.5",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/gHy3eh_Ad8iN",
		"status" : 1
	},
	{
		"idx" : 1060,
		"title" : "이치고",
		"score" : "4.5",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/f9Y2khRVShoF",
		"status" : 1
	},
	{
		"idx" : 1061,
		"title" : "뉴질랜드스토리",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/H6EKPX1ASO",
		"status" : 1
	},
	{
		"idx" : 1062,
		"title" : "한아람",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/6uwqywv4T8",
		"status" : 1
	},
	{
		"idx" : 1063,
		"title" : "고든램지버거",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/FsBMnKG8dBZs",
		"status" : 1
	},
	{
		"idx" : 1064,
		"title" : "오레노라멘",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/3hBVUKv8fj2M",
		"status" : 1
	},
	{
		"idx" : 1065,
		"title" : "콰이어트 크림티",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/dPMQH4nlqZXc",
		"status" : 1
	},
	{
		"idx" : 1066,
		"title" : "라미아파밀리아",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/K72n2CbmYubj",
		"status" : 1
	},
	{
		"idx" : 1067,
		"title" : "더마칸",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/PAVVg2WfDd9d",
		"status" : 1
	},
	{
		"idx" : 1068,
		"title" : "라오빠빠",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/LVixjKB0N9TZ",
		"status" : 1
	},
	{
		"idx" : 1069,
		"title" : "선호커피로스터스",
		"score" : "4.4",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/za8nNoJlLchp",
		"status" : 1
	},
	{
		"idx" : 1070,
		"title" : "흥도식당",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/6kf24WCninDE",
		"status" : 1
	},
	{
		"idx" : 1071,
		"title" : "해주찹쌀순대",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/lh1FOMT0A8",
		"status" : 1
	},
	{
		"idx" : 1072,
		"title" : "명서식당",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/7FCWNRj5jd4q",
		"status" : 1
	},
	{
		"idx" : 1073,
		"title" : "잠수교집",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/EL7KF5Pi1SfG",
		"status" : 1
	},
	{
		"idx" : 1074,
		"title" : "피제리아다븟",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/T2Dt8XC6dn5g",
		"status" : 1
	},
	{
		"idx" : 1075,
		"title" : "놀부유황오리진흙구이",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/Ix_DhPTFji",
		"status" : 1
	},
	{
		"idx" : 1076,
		"title" : "자몽하다",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/cnWxRB1twbDy",
		"status" : 1
	},
	{
		"idx" : 1077,
		"title" : "모타운 서울",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/akp8D-Zgbuno",
		"status" : 1
	},
	{
		"idx" : 1078,
		"title" : "우프",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/hqBbvCR3Uq_q",
		"status" : 1
	},
	{
		"idx" : 1079,
		"title" : "코스모스시",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/S8V0useyH0QU",
		"status" : 1
	},
	{
		"idx" : 1080,
		"title" : "바토스",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/EVh4TgJsb5",
		"status" : 1
	},
	{
		"idx" : 1081,
		"title" : "얼터너티브",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/5tMP44aXiA34",
		"status" : 1
	},
	{
		"idx" : 1082,
		"title" : "알라딘의양고기",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/QHuJWAVoYo",
		"status" : 1
	},
	{
		"idx" : 1083,
		"title" : "갓잇",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/dfDGrM_Gt5sO",
		"status" : 1
	},
	{
		"idx" : 1084,
		"title" : "사카바게라게라",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/PS0zk1W_A_mY",
		"status" : 1
	},
	{
		"idx" : 1085,
		"title" : "함경도찹쌀순대",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/xNYy1JKe-6",
		"status" : 1
	},
	{
		"idx" : 1086,
		"title" : "브럭시",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/WL6Rkaz88Zmy",
		"status" : 1
	},
	{
		"idx" : 1087,
		"title" : "니커버커베이글",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/4Nd5tgywZPhK",
		"status" : 1
	},
	{
		"idx" : 1088,
		"title" : "육분삼십",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/3-6X2rdMrTFE",
		"status" : 1
	},
	{
		"idx" : 1089,
		"title" : "쥬뗑뷔뜨",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/s7x431dKb54e",
		"status" : 1
	},
	{
		"idx" : 1090,
		"title" : "쟈뎅디베르",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/ujFsBhqWxv9f",
		"status" : 1
	},
	{
		"idx" : 1091,
		"title" : "정가네 순뎅이",
		"score" : "4.3",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/8ED_vcBCZ-iP",
		"status" : 1
	},
	{
		"idx" : 1092,
		"title" : "그리지하우스",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/emXSlMxnQh",
		"status" : 1
	},
	{
		"idx" : 1093,
		"title" : "옥인피자",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/c-BO2-JZg1",
		"status" : 1
	},
	{
		"idx" : 1094,
		"title" : "뷰클런즈",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/-CD30XiIxc0s",
		"status" : 1
	},
	{
		"idx" : 1095,
		"title" : "모터시티",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/n7UTzGp2eTu8",
		"status" : 1
	},
	{
		"idx" : 1096,
		"title" : "비채나",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/cLELTgFyY3nZ",
		"status" : 1
	},
	{
		"idx" : 1097,
		"title" : "부일갈매기",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/RmWnk3N282",
		"status" : 1
	},
	{
		"idx" : 1098,
		"title" : "하얼빈양꼬치",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/JyVLCx6S6-",
		"status" : 1
	},
	{
		"idx" : 1099,
		"title" : "팀호완",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/rs2l3jwk3yzh",
		"status" : 1
	},
	{
		"idx" : 1100,
		"title" : "라뿔",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/62elqYKWWPVK",
		"status" : 1
	},
	{
		"idx" : 1101,
		"title" : "네기우나기야",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/q6opDDXJGOvx",
		"status" : 1
	},
	{
		"idx" : 1102,
		"title" : "주점금붕어",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/KsEuD26DD79V",
		"status" : 1
	},
	{
		"idx" : 1103,
		"title" : "촙촙",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/DPoaAgfqScmb",
		"status" : 1
	},
	{
		"idx" : 1104,
		"title" : "이경진우렁쌈밥정식",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/H9B75P0dmy",
		"status" : 1
	},
	{
		"idx" : 1105,
		"title" : "방이샤브샤브칼국수",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/Vt5DL-BRC5",
		"status" : 1
	},
	{
		"idx" : 1106,
		"title" : "오징어세상",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/m-Ed11yxur",
		"status" : 1
	},
	{
		"idx" : 1107,
		"title" : "마초야",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/LOZOoFM8xA7M",
		"status" : 1
	},
	{
		"idx" : 1108,
		"title" : "하우스서울",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/IU7rqeXPw5Dh",
		"status" : 1
	},
	{
		"idx" : 1109,
		"title" : "정목누룽지백숙",
		"score" : "4.2",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/OgQVIAit2YBW",
		"status" : 1
	},
	{
		"idx" : 1110,
		"title" : "봉피양",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/OEN8Bp7Cgyag",
		"status" : 1
	},
	{
		"idx" : 1111,
		"title" : "부부횟집",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/G0JDxLuKFr",
		"status" : 1
	},
	{
		"idx" : 1112,
		"title" : "오로라경양식",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/Y0xtXbEgiQ4d",
		"status" : 1
	},
	{
		"idx" : 1113,
		"title" : "츠쿠모",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/e25D3FrOAs9N",
		"status" : 1
	},
	{
		"idx" : 1114,
		"title" : "개군할머니토종순대국",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/1sDuKZHGRcoo",
		"status" : 1
	},
	{
		"idx" : 1115,
		"title" : "디라이프스타일키친",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/S7vDe_YR_LFU",
		"status" : 1
	},
	{
		"idx" : 1116,
		"title" : "효모",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/x0ZbnVI0c6gY",
		"status" : 1
	},
	{
		"idx" : 1117,
		"title" : "화덕고깃간",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/y7g4l0AJPGe6",
		"status" : 1
	},
	{
		"idx" : 1118,
		"title" : "도꼭지",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/culb0Kt0JxUO",
		"status" : 1
	},
	{
		"idx" : 1119,
		"title" : "서래냉면",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/1KJMX9ASqx",
		"status" : 1
	},
	{
		"idx" : 1120,
		"title" : "부미면옥",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/6GDmCZoQUU8F",
		"status" : 1
	},
	{
		"idx" : 1121,
		"title" : "시부야돈까스",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/Pu7eAoTOqx8l",
		"status" : 1
	},
	{
		"idx" : 1122,
		"title" : "진대감",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/uhIbDTDBf8hC",
		"status" : 1
	},
	{
		"idx" : 1123,
		"title" : "산들해",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/5jJOBBcLv4",
		"status" : 1
	},
	{
		"idx" : 1124,
		"title" : "리나스",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/7DEKXufy_Ib7",
		"status" : 1
	},
	{
		"idx" : 1125,
		"title" : "신천샤브칼국수",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/lcNwW86Hls",
		"status" : 1
	},
	{
		"idx" : 1126,
		"title" : "호이안로스터리",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/OgcSeqzcFvGa",
		"status" : 1
	},
	{
		"idx" : 1127,
		"title" : "엄지손칼국수",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/LB939Xp8PH",
		"status" : 1
	},
	{
		"idx" : 1128,
		"title" : "중화일상",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/H0Pf_dEpr5nK",
		"status" : 1
	},
	{
		"idx" : 1129,
		"title" : "풍년뼈다귀해장국",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/zVS6lOHKCk",
		"status" : 1
	},
	{
		"idx" : 1130,
		"title" : "신의주부대찌개",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/iB9ZXOGLqE",
		"status" : 1
	},
	{
		"idx" : 1131,
		"title" : "명인밥상",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/US2mswa9am6o",
		"status" : 1
	},
	{
		"idx" : 1132,
		"title" : "나루모듬전",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/jhnsBeunhFuH",
		"status" : 1
	},
	{
		"idx" : 1133,
		"title" : "홍코너",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/72ERZX8gFA",
		"status" : 1
	},
	{
		"idx" : 1134,
		"title" : "샐그릭",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/gVRl1wwwL63S",
		"status" : 1
	},
	{
		"idx" : 1135,
		"title" : "용용선생",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/7j_-Lcb_qqo6",
		"status" : 1
	},
	{
		"idx" : 1136,
		"title" : "비사벌전주콩나물국밥",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/6_F5BumpWl",
		"status" : 1
	},
	{
		"idx" : 1137,
		"title" : "꼬치집",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/h-xfHrtIIzMP",
		"status" : 1
	},
	{
		"idx" : 1138,
		"title" : "전국낙지자랑",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/8Rm95EOVKl67",
		"status" : 1
	},
	{
		"idx" : 1139,
		"title" : "바이킹스워프",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/VUw7BCxrpE",
		"status" : 1
	},
	{
		"idx" : 1140,
		"title" : "프로퍼커피바",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/UobeqW4wII",
		"status" : 1
	},
	{
		"idx" : 1141,
		"title" : "진저베어",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/WyYCC0Wq-AHp",
		"status" : 1
	},
	{
		"idx" : 1142,
		"title" : "스시산",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/JDCsMvL3X5",
		"status" : 1
	},
	{
		"idx" : 1143,
		"title" : "고도식",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/DoM3VbHErGBl",
		"status" : 1
	},
	{
		"idx" : 1144,
		"title" : "이월로스터스",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/cP3Eq-mUKf9e",
		"status" : 1
	},
	{
		"idx" : 1145,
		"title" : "스시작",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/JaBcDxtQ4Fsl",
		"status" : 1
	},
	{
		"idx" : 1146,
		"title" : "라세느",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/ttYAw6tpj6",
		"status" : 1
	},
	{
		"idx" : 1147,
		"title" : "모토쿠라시",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/-NshQhMCGKUd",
		"status" : 1
	},
	{
		"idx" : 1148,
		"title" : "르빵",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/yMqkgBjHH7",
		"status" : 1
	},
	{
		"idx" : 1149,
		"title" : "도삭면공방",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/S_Nu2odL9so9",
		"status" : 1
	},
	{
		"idx" : 1150,
		"title" : "현차이나",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/zCpGNVc9sqng",
		"status" : 1
	},
	{
		"idx" : 1151,
		"title" : "소담 안동국시",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/b6DXhQ8IDHWs",
		"status" : 1
	},
	{
		"idx" : 1152,
		"title" : "테이크어샤워",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/l3pRKCV7yDOl",
		"status" : 1
	},
	{
		"idx" : 1153,
		"title" : "익형주방",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/Jn3pxt2vCDI7",
		"status" : 1
	},
	{
		"idx" : 1154,
		"title" : "진원조닭한마리",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/sS0TQkMd2w",
		"status" : 1
	},
	{
		"idx" : 1155,
		"title" : "삼청각",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/RYzmLQ_v5h",
		"status" : 1
	},
	{
		"idx" : 1156,
		"title" : "단디",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/HySGClEDoTf8",
		"status" : 1
	},
	{
		"idx" : 1157,
		"title" : "별미곱창",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/P5OfZLHFHF",
		"status" : 1
	},
	{
		"idx" : 1158,
		"title" : "트레스드",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/PXQ_6PMjrpVl",
		"status" : 1
	},
	{
		"idx" : 1159,
		"title" : "할머니포장마차멸치국수",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/PX7RWNtD9w",
		"status" : 1
	},
	{
		"idx" : 1160,
		"title" : "더이탈리안클럽",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/th321zQf3IyS",
		"status" : 1
	},
	{
		"idx" : 1161,
		"title" : "콩당콩당",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/Qp62DG4Icilv",
		"status" : 1
	},
	{
		"idx" : 1162,
		"title" : "소담정",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/y3V_EypZ5ECd",
		"status" : 1
	},
	{
		"idx" : 1163,
		"title" : "청와옥",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/P85YwL15FTAT",
		"status" : 1
	},
	{
		"idx" : 1164,
		"title" : "오복수산",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/7Fif7rvC3g4t",
		"status" : 1
	},
	{
		"idx" : 1165,
		"title" : "라멘쨩",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/z2kfP6yR1ILm",
		"status" : 1
	},
	{
		"idx" : 1166,
		"title" : "콘메",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/Senr4ZgwxGa6",
		"status" : 1
	},
	{
		"idx" : 1167,
		"title" : "라이언하트",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/DrAglGTkfBY0",
		"status" : 1
	},
	{
		"idx" : 1168,
		"title" : "황산냉면",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/bspgaNW1EOEj",
		"status" : 1
	},
	{
		"idx" : 1169,
		"title" : "바렌나 에스프레소바",
		"score" : "4.0",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/01gMWX7dyMCA",
		"status" : 1
	},
	{
		"idx" : 1170,
		"title" : "큐스시",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/73oprrduh0",
		"status" : 1
	},
	{
		"idx" : 1171,
		"title" : "파티세리김영모",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/NI6PbBUeYs",
		"status" : 1
	},
	{
		"idx" : 1172,
		"title" : "식당 NeO",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/ONIEiPq6eQuC",
		"status" : 1
	},
	{
		"idx" : 1173,
		"title" : "차고버거",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/o-3WeuB_EcAF",
		"status" : 1
	},
	{
		"idx" : 1174,
		"title" : "니꾸바시야",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/l6I9MqrfkChr",
		"status" : 1
	},
	{
		"idx" : 1175,
		"title" : "초이스시",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/W3hwhMg7Ddr6",
		"status" : 1
	},
	{
		"idx" : 1176,
		"title" : "청화초밥",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/Pp2asSMMQwcf",
		"status" : 1
	},
	{
		"idx" : 1177,
		"title" : "딤딤섬",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/0YXwdiCN3pAb",
		"status" : 1
	},
	{
		"idx" : 1178,
		"title" : "페메종",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/sed8ib6p7TeO",
		"status" : 1
	},
	{
		"idx" : 1179,
		"title" : "Murmur",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/l4lflCWOyh0H",
		"status" : 1
	},
	{
		"idx" : 1180,
		"title" : "노란상소갈비",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/JZnoG3NUJjBQ",
		"status" : 1
	},
	{
		"idx" : 1181,
		"title" : "가락골마산아구찜",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/aAeB4WEkUD",
		"status" : 1
	},
	{
		"idx" : 1182,
		"title" : "칫챗",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/Fzc4tF5Zp5p_",
		"status" : 1
	},
	{
		"idx" : 1183,
		"title" : "홀짝집",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/g8-7qxvhichO",
		"status" : 1
	},
	{
		"idx" : 1184,
		"title" : "포유티",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/GjpkTNLb_AeP",
		"status" : 1
	},
	{
		"idx" : 1185,
		"title" : "가일",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/dhJ4DJyC5q",
		"status" : 1
	},
	{
		"idx" : 1186,
		"title" : "연어식당",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/7LeH2dfX6t7P",
		"status" : 1
	},
	{
		"idx" : 1187,
		"title" : "보길",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/w4aBvbOCCjRs",
		"status" : 1
	},
	{
		"idx" : 1188,
		"title" : "장칼집",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/WUmPSgM5vPLC",
		"status" : 1
	},
	{
		"idx" : 1189,
		"title" : "늘푸른목장",
		"score" : "3.9",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/rew7gTaYu5",
		"status" : 1
	},
	{
		"idx" : 1190,
		"title" : "온달수산",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/32oIwNkHIm",
		"status" : 1
	},
	{
		"idx" : 1191,
		"title" : "오스테리아세콘디",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/BkAe_55mbnya",
		"status" : 1
	},
	{
		"idx" : 1192,
		"title" : "원산만두",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/SJfY43e9Hl",
		"status" : 1
	},
	{
		"idx" : 1193,
		"title" : "양군스시&참치",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/h2RQ42TshKwP",
		"status" : 1
	},
	{
		"idx" : 1194,
		"title" : "카레바시야",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/RR2K01YxqmbL",
		"status" : 1
	},
	{
		"idx" : 1195,
		"title" : "커피앰비언스",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/PppdkDuAmE",
		"status" : 1
	},
	{
		"idx" : 1196,
		"title" : "우직",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/u6c-7NYSvdOy",
		"status" : 1
	},
	{
		"idx" : 1197,
		"title" : "컨플릭트스토어",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/4owletMd90R5",
		"status" : 1
	},
	{
		"idx" : 1198,
		"title" : "명가수산",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/k2nL-CjxhyCP",
		"status" : 1
	},
	{
		"idx" : 1199,
		"title" : "문정돈",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/gS5pZZevZcHx",
		"status" : 1
	},
	{
		"idx" : 1200,
		"title" : "그릴210버거",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/kzF8HtXmDhZ_",
		"status" : 1
	},
	{
		"idx" : 1201,
		"title" : "만주",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/hPybdDitvbhp",
		"status" : 1
	},
	{
		"idx" : 1202,
		"title" : "한국계",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/jSy3uIxv33yb",
		"status" : 1
	},
	{
		"idx" : 1203,
		"title" : "온수반",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/WP-s_BQfybIE",
		"status" : 1
	},
	{
		"idx" : 1204,
		"title" : "흥도식당",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/j2eZLBTeGXzk",
		"status" : 1
	},
	{
		"idx" : 1205,
		"title" : "TWG 티룸",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/pRmmI5Jayu",
		"status" : 1
	},
	{
		"idx" : 1206,
		"title" : "도니족발",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/0P_wdf0wl8",
		"status" : 1
	},
	{
		"idx" : 1207,
		"title" : "오터",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/J-WpTLuK4PeG",
		"status" : 1
	},
	{
		"idx" : 1208,
		"title" : "본가진미간장게장",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/ahPOx7rAcA",
		"status" : 1
	},
	{
		"idx" : 1209,
		"title" : "보틀벙커",
		"score" : "4.1",
		"region" : "송파구",
		"url" : "https://www.mangoplate.com/restaurants/OAP0rlo_oySj",
		"status" : 1
	},
	{
		"idx" : 1210,
		"title" : "쭈꾸쭈꾸쭈꾸미",
		"score" : "4.1",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/Gzu9n6Sa9W",
		"status" : 1
	},
	{
		"idx" : 1211,
		"title" : "풍년상회쪽갈비",
		"score" : "4.1",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/nx2dZEWZtg",
		"status" : 1
	},
	{
		"idx" : 1212,
		"title" : "꿀꿀진순대국",
		"score" : "4.1",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/NqE-OchUTTj7",
		"status" : 1
	},
	{
		"idx" : 1213,
		"title" : "똥찌비",
		"score" : "4.1",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/Tgxi5HX9iPsY",
		"status" : 1
	},
	{
		"idx" : 1214,
		"title" : "경양미식",
		"score" : "4.1",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/P-B10eFaNbHX",
		"status" : 1
	},
	{
		"idx" : 1215,
		"title" : "대팔이네",
		"score" : "4.1",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/_yADsOjr5WLX",
		"status" : 1
	},
	{
		"idx" : 1216,
		"title" : "화진포막국수",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/v3HPIb2VWJ",
		"status" : 1
	},
	{
		"idx" : 1217,
		"title" : "앙상블",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/yGruzkqTb9Fs",
		"status" : 1
	},
	{
		"idx" : 1218,
		"title" : "멘야세븐",
		"score" : "3.4",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/hOj6PPauFmjT",
		"status" : 1
	},
	{
		"idx" : 1219,
		"title" : "모범떡볶이 1976",
		"score" : "3.4",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/GY4qEYGpXf",
		"status" : 1
	},
	{
		"idx" : 1220,
		"title" : "이자카야 인",
		"score" : "3.4",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/cBBvuxH02LCB",
		"status" : 1
	},
	{
		"idx" : 1221,
		"title" : "스시마에",
		"score" : "3.3",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/nWeCoq9KF7x6",
		"status" : 1
	},
	{
		"idx" : 1222,
		"title" : "긴자",
		"score" : "3.3",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/8kgyfKPGEo",
		"status" : 1
	},
	{
		"idx" : 1223,
		"title" : "차이나린찐",
		"score" : "3.2",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/X085Rss8xj",
		"status" : 1
	},
	{
		"idx" : 1224,
		"title" : "분홍다이닝",
		"score" : "3.2",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/E_Fz8w5y18",
		"status" : 1
	},
	{
		"idx" : 1225,
		"title" : "유타로",
		"score" : "3.2",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/VwPBQcYROU",
		"status" : 1
	},
	{
		"idx" : 1226,
		"title" : "아키노유키",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/5QXC2WprQA",
		"status" : 1
	},
	{
		"idx" : 1227,
		"title" : "채스우드커피",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/kWv07kX09tUU",
		"status" : 1
	},
	{
		"idx" : 1228,
		"title" : "통로",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/RRz_jdgpZeKF",
		"status" : 1
	},
	{
		"idx" : 1229,
		"title" : "하루노유키",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/hr_13jsN4rv9",
		"status" : 1
	},
	{
		"idx" : 1230,
		"title" : "반피셋",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/_Swst80B2dJV",
		"status" : 1
	},
	{
		"idx" : 1231,
		"title" : "푸지미곱창",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/NmAVkF6R2hk9",
		"status" : 1
	},
	{
		"idx" : 1232,
		"title" : "아이아오",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/Drl7Sjj0FZ2x",
		"status" : 1
	},
	{
		"idx" : 1233,
		"title" : "서울 감자탕",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/WYrfx6n8Oiaa",
		"status" : 1
	},
	{
		"idx" : 1234,
		"title" : "미분당",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/7RCBaHvUEkBg",
		"status" : 1
	},
	{
		"idx" : 1235,
		"title" : "백년화편",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/YElZDILTrW",
		"status" : 1
	},
	{
		"idx" : 1236,
		"title" : "구삼부대찌개",
		"score" : "4.0",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/xczNktyrTdPm",
		"status" : 1
	},
	{
		"idx" : 1237,
		"title" : "카쿠",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/fvU-WRzL7sQp",
		"status" : 1
	},
	{
		"idx" : 1238,
		"title" : "이한진숙성회",
		"score" : "4.5",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/yHgtnFi6JVKB",
		"status" : 1
	},
	{
		"idx" : 1239,
		"title" : "대성반점",
		"score" : "4.4",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/OtG4tNP0bJ",
		"status" : 1
	},
	{
		"idx" : 1240,
		"title" : "신흥정육식당",
		"score" : "4.4",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/10JjveRoc_N1",
		"status" : 1
	},
	{
		"idx" : 1241,
		"title" : "스시공간",
		"score" : "4.4",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/80zTWPhMQLmQ",
		"status" : 1
	},
	{
		"idx" : 1242,
		"title" : "진미한우곱창",
		"score" : "4.3",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/PzI0ZmOKv54M",
		"status" : 1
	},
	{
		"idx" : 1243,
		"title" : "고모네원조콩탕북어탕",
		"score" : "4.3",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/1RQQBv2FPC",
		"status" : 1
	},
	{
		"idx" : 1244,
		"title" : "등갈비달인",
		"score" : "4.3",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/ceauoy6f7CPf",
		"status" : 1
	},
	{
		"idx" : 1245,
		"title" : "우리동네막국수국밥",
		"score" : "4.3",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/UgPfm9gXmSgE",
		"status" : 1
	},
	{
		"idx" : 1246,
		"title" : "영화정해장국",
		"score" : "4.3",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/6pnvpBumIrjg",
		"status" : 1
	},
	{
		"idx" : 1247,
		"title" : "소문난칼국수",
		"score" : "4.3",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/0Ck__3lGsq",
		"status" : 1
	},
	{
		"idx" : 1248,
		"title" : "방콕,그집",
		"score" : "4.3",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/WVmnI8Tyis4Q",
		"status" : 1
	},
	{
		"idx" : 1249,
		"title" : "다람",
		"score" : "4.2",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/ScCnZ6CGpz",
		"status" : 1
	},
	{
		"idx" : 1250,
		"title" : "얌얌카츠",
		"score" : "4.2",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/x-wh7Hgs9oQP",
		"status" : 1
	},
	{
		"idx" : 1251,
		"title" : "담금",
		"score" : "4.2",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/-srG9TS2F6R_",
		"status" : 1
	},
	{
		"idx" : 1252,
		"title" : "시장횟집",
		"score" : "4.2",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/adQFaqjq2w6Q",
		"status" : 1
	},
	{
		"idx" : 1253,
		"title" : "말뚝곱창",
		"score" : "4.2",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/_4_zru5KKTbR",
		"status" : 1
	},
	{
		"idx" : 1254,
		"title" : "보타이",
		"score" : "4.1",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/J7QQDI77g3YC",
		"status" : 1
	},
	{
		"idx" : 1255,
		"title" : "커피몽타주",
		"score" : "4.1",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/BporjXQf3c",
		"status" : 1
	},
	{
		"idx" : 1256,
		"title" : "유미벅스",
		"score" : "4.1",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/l6m061vFqA",
		"status" : 1
	},
	{
		"idx" : 1257,
		"title" : "봉래면옥",
		"score" : "4.1",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/WOaP1-KVWysz",
		"status" : 1
	},
	{
		"idx" : 1258,
		"title" : "블랑제리 11 17",
		"score" : "3.7",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/r8YSEe2sFs",
		"status" : 1
	},
	{
		"idx" : 1259,
		"title" : "솜솜베이커리",
		"score" : "3.7",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/G_IYcwWAStXf",
		"status" : 1
	},
	{
		"idx" : 1260,
		"title" : "에이컷스테이크",
		"score" : "3.7",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/avYS8SURZp",
		"status" : 1
	},
	{
		"idx" : 1261,
		"title" : "피에로커피",
		"score" : "3.7",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/4Xwx_fbC3Myj",
		"status" : 1
	},
	{
		"idx" : 1262,
		"title" : "프언타이",
		"score" : "3.7",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/1BBuC73-mKic",
		"status" : 1
	},
	{
		"idx" : 1263,
		"title" : "연풍민락",
		"score" : "3.7",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/6Mc1Zg38I9fF",
		"status" : 1
	},
	{
		"idx" : 1264,
		"title" : "미드데이썬",
		"score" : "3.7",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/6OJL7YQTdCpV",
		"status" : 1
	},
	{
		"idx" : 1265,
		"title" : "모리식당",
		"score" : "3.7",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/GCGwjmtIlz-s",
		"status" : 1
	},
	{
		"idx" : 1266,
		"title" : "셀프하우스",
		"score" : "3.6",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/cnNNWcYjvp",
		"status" : 1
	},
	{
		"idx" : 1267,
		"title" : "하이몬드",
		"score" : "3.6",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/9C0ettg0CQ",
		"status" : 1
	},
	{
		"idx" : 1268,
		"title" : "하다식당",
		"score" : "3.6",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/Wm43kPZq_Q7b",
		"status" : 1
	},
	{
		"idx" : 1269,
		"title" : "미니회바",
		"score" : "3.6",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/gU1rSYRKK6",
		"status" : 1
	},
	{
		"idx" : 1270,
		"title" : "평양만두집",
		"score" : "3.6",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/rxmjZzTJ6R",
		"status" : 1
	},
	{
		"idx" : 1271,
		"title" : "안녕식당",
		"score" : "3.5",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/eZ4qHgtH6w",
		"status" : 1
	},
	{
		"idx" : 1272,
		"title" : "스윗솔트",
		"score" : "3.5",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/SQMAH5-3dFW8",
		"status" : 1
	},
	{
		"idx" : 1273,
		"title" : "풀팬",
		"score" : "3.5",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/YF8Jmr7mMc",
		"status" : 1
	},
	{
		"idx" : 1274,
		"title" : "스시야미",
		"score" : "3.5",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/2C6y6rYByR",
		"status" : 1
	},
	{
		"idx" : 1275,
		"title" : "파트원나이스",
		"score" : "3.5",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/Sq37hIF0sMiA",
		"status" : 1
	},
	{
		"idx" : 1276,
		"title" : "해중천반점",
		"score" : "3.5",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/jgdHAgVJM3",
		"status" : 1
	},
	{
		"idx" : 1277,
		"title" : "인정원월남쌈",
		"score" : "3.5",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/FLSvKO8-xY",
		"status" : 1
	},
	{
		"idx" : 1278,
		"title" : "송하정스시",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/Qqg6wsJuxP0G",
		"status" : 1
	},
	{
		"idx" : 1279,
		"title" : "온온",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/yxHKlo87wste",
		"status" : 1
	},
	{
		"idx" : 1280,
		"title" : "히든브라운",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/YXlLO-s1FSfN",
		"status" : 1
	},
	{
		"idx" : 1281,
		"title" : "갓잇",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/1Gth5eAmJrSX",
		"status" : 1
	},
	{
		"idx" : 1282,
		"title" : "빠네렌토",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/k1u2u3QtWw",
		"status" : 1
	},
	{
		"idx" : 1283,
		"title" : "카페온도",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/E8AJSMuCLkez",
		"status" : 1
	},
	{
		"idx" : 1284,
		"title" : "애크로매틱 커피 컴퍼니",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/RoMRPEgbdANq",
		"status" : 1
	},
	{
		"idx" : 1285,
		"title" : "족발선생",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/MW09IHHOIL54",
		"status" : 1
	},
	{
		"idx" : 1286,
		"title" : "시집그릴하우스",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/sow2OMed9_mj",
		"status" : 1
	},
	{
		"idx" : 1287,
		"title" : "마드레",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/75JsQUDUgi",
		"status" : 1
	},
	{
		"idx" : 1288,
		"title" : "천호누룽지통닭구이",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/wVlt1-AwOzL_",
		"status" : 1
	},
	{
		"idx" : 1289,
		"title" : "두리돈까스",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/Spc1PXAhCY",
		"status" : 1
	},
	{
		"idx" : 1290,
		"title" : "월요일",
		"score" : "3.9",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/M_tYT7fjKkmX",
		"status" : 1
	},
	{
		"idx" : 1291,
		"title" : "분더버거",
		"score" : "3.8",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/ob-bxH8c3Wl7",
		"status" : 1
	},
	{
		"idx" : 1292,
		"title" : "황푸차이나",
		"score" : "3.8",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/vAks8hBiGB8I",
		"status" : 1
	},
	{
		"idx" : 1293,
		"title" : "강동호치민",
		"score" : "3.8",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/2HM7cryjOquH",
		"status" : 1
	},
	{
		"idx" : 1294,
		"title" : "송월냉면",
		"score" : "3.8",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/KMdKf9fFfSuZ",
		"status" : 1
	},
	{
		"idx" : 1295,
		"title" : "진이네떡볶이",
		"score" : "3.8",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/lLT__Mf-fm",
		"status" : 1
	},
	{
		"idx" : 1296,
		"title" : "YUP",
		"score" : "3.8",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/2LabZpVKWOSf",
		"status" : 1
	},
	{
		"idx" : 1297,
		"title" : "브로일링커피컴퍼니",
		"score" : "3.8",
		"region" : "강동구",
		"url" : "https://www.mangoplate.com/restaurants/ZVSjVnU35HkK",
		"status" : 1
	},
	{
		"idx" : 1298,
		"title" : "나루토 오모테나시",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/HWI4rONixoXD",
		"status" : 1
	},
	{
		"idx" : 1299,
		"title" : "우동 이요이요",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/BzvUd3QUxApO",
		"status" : 1
	},
	{
		"idx" : 1300,
		"title" : "멕시코식당",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/zSujg5KWKY1W",
		"status" : 1
	},
	{
		"idx" : 1301,
		"title" : "제스티살룬",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/A5NeU-FXeh6z",
		"status" : 1
	},
	{
		"idx" : 1302,
		"title" : "마루심",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/IO9dLs7lCwL6",
		"status" : 1
	},
	{
		"idx" : 1303,
		"title" : "비파티세리",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/AKBv9lvYHqag",
		"status" : 1
	},
	{
		"idx" : 1304,
		"title" : "Osteria Ora",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/BOYPLw_sEbew",
		"status" : 1
	},
	{
		"idx" : 1305,
		"title" : "윤서울",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/uQN8yVGdvqsP",
		"status" : 1
	},
	{
		"idx" : 1306,
		"title" : "삼월황",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/DTHwgfPohyXQ",
		"status" : 1
	},
	{
		"idx" : 1307,
		"title" : "멜로즈",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/AG1y-UfdJ4LR",
		"status" : 1
	},
	{
		"idx" : 1308,
		"title" : "코랏",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/XKTpqB5d4rPl",
		"status" : 1
	},
	{
		"idx" : 1309,
		"title" : "차차티클럽",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/V9RbJdbdgBDb",
		"status" : 1
	},
	{
		"idx" : 1310,
		"title" : "그리스마스",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/iXuHrrVTz2ow",
		"status" : 1
	},
	{
		"idx" : 1311,
		"title" : "옥자",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/EVtIwxao-fXi",
		"status" : 1
	},
	{
		"idx" : 1312,
		"title" : "키노키친",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/-NtLHShgnYm2",
		"status" : 1
	},
	{
		"idx" : 1313,
		"title" : "상암회관",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/onGDjypuMJMF",
		"status" : 1
	},
	{
		"idx" : 1314,
		"title" : "리밀앤밀리",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/eUEiZOaEEFHH",
		"status" : 1
	},
	{
		"idx" : 1315,
		"title" : "셔우드",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/Pq9hn8HNhCRk",
		"status" : 1
	},
	{
		"idx" : 1316,
		"title" : "조이버거",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/YN8fxJ-2aGmS",
		"status" : 1
	},
	{
		"idx" : 1317,
		"title" : "전주상회",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/nhRklnCx5Nss",
		"status" : 1
	},
	{
		"idx" : 1318,
		"title" : "이안정",
		"score" : "4.8",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/SapvvirrPYwo",
		"status" : 1
	},
	{
		"idx" : 1319,
		"title" : "멘타카무쇼",
		"score" : "4.8",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/V1pDpcDIntci",
		"status" : 1
	},
	{
		"idx" : 1320,
		"title" : "카와카츠",
		"score" : "4.7",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/HHxp24PCqgZn",
		"status" : 1
	},
	{
		"idx" : 1321,
		"title" : "야키토리나루토",
		"score" : "4.7",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/-SvQDki5HNzQ",
		"status" : 1
	},
	{
		"idx" : 1322,
		"title" : "소점",
		"score" : "4.7",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/Ru3a_egfnE5L",
		"status" : 1
	},
	{
		"idx" : 1323,
		"title" : "파델라",
		"score" : "4.7",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/jir8uDJCA14B",
		"status" : 1
	},
	{
		"idx" : 1324,
		"title" : "우주옥",
		"score" : "4.7",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/ogLsfHRX4bR1",
		"status" : 1
	},
	{
		"idx" : 1325,
		"title" : "조앤도슨",
		"score" : "4.7",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/qs2kK_LDx0fU",
		"status" : 1
	},
	{
		"idx" : 1326,
		"title" : "로랑",
		"score" : "4.7",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/Vlra2186dEl7",
		"status" : 1
	},
	{
		"idx" : 1327,
		"title" : "무겐스위치",
		"score" : "4.7",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/SdbBGGIUIdRR",
		"status" : 1
	},
	{
		"idx" : 1328,
		"title" : "카와카츠",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/KoWdFMdQ5L8L",
		"status" : 1
	},
	{
		"idx" : 1329,
		"title" : "라바즈",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/MMEELt3usvci",
		"status" : 1
	},
	{
		"idx" : 1330,
		"title" : "엘리스리틀이태리",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/zqa4ktmPw3hA",
		"status" : 1
	},
	{
		"idx" : 1331,
		"title" : "야망",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/nW33naPLZZXD",
		"status" : 1
	},
	{
		"idx" : 1332,
		"title" : "담택",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/A2WMRSbPSYb_",
		"status" : 1
	},
	{
		"idx" : 1333,
		"title" : "기노",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/11oIVuDS6iYo",
		"status" : 1
	},
	{
		"idx" : 1334,
		"title" : "고미태",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/Lz_ubT1nJ_sc",
		"status" : 1
	},
	{
		"idx" : 1335,
		"title" : "아소토",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/1PJfkVvvhrig",
		"status" : 1
	},
	{
		"idx" : 1336,
		"title" : "웨스트사이드",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/qW3awC-XO2AL",
		"status" : 1
	},
	{
		"idx" : 1337,
		"title" : "히비카레빵집",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/a3ecam2pRihd",
		"status" : 1
	},
	{
		"idx" : 1338,
		"title" : "카밀로라자네리아",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/_CsDWQgkZXoc",
		"status" : 1
	},
	{
		"idx" : 1339,
		"title" : "빠넬로",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/c74WdbCYvI",
		"status" : 1
	},
	{
		"idx" : 1340,
		"title" : "교다이야",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/DG9WuFwF8U",
		"status" : 1
	},
	{
		"idx" : 1341,
		"title" : "복덕방",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/5e4Lb-iMjNo5",
		"status" : 1
	},
	{
		"idx" : 1342,
		"title" : "라무라",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/I-kkCnpK8aV9",
		"status" : 1
	},
	{
		"idx" : 1343,
		"title" : "스파카나폴리",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/56aWuL_8Hb",
		"status" : 1
	},
	{
		"idx" : 1344,
		"title" : "최강금돈까스",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/S8jFDbhGKykh",
		"status" : 1
	},
	{
		"idx" : 1345,
		"title" : "원조 조박집",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/BK53Qu73ke",
		"status" : 1
	},
	{
		"idx" : 1346,
		"title" : "라뚜셩트",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/N4x8dwjiLxdS",
		"status" : 1
	},
	{
		"idx" : 1347,
		"title" : "티크닉",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/SaCJTvz6fPV8",
		"status" : 1
	},
	{
		"idx" : 1348,
		"title" : "화상손만두",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/kMCZauqNZL",
		"status" : 1
	},
	{
		"idx" : 1349,
		"title" : "퀜치커피",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/WwryVYxyp6XI",
		"status" : 1
	},
	{
		"idx" : 1350,
		"title" : "아꽁뜨",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/DBLym1DsA0t3",
		"status" : 1
	},
	{
		"idx" : 1351,
		"title" : "헤키",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/ATfM4AsMzFcZ",
		"status" : 1
	},
	{
		"idx" : 1352,
		"title" : "쿄라멘",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/0on9-e46dwvb",
		"status" : 1
	},
	{
		"idx" : 1353,
		"title" : "코메아벨렘",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/1wuy7OLPF6RB",
		"status" : 1
	},
	{
		"idx" : 1354,
		"title" : "숙성육관",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/IpF3Adr6JcG3",
		"status" : 1
	},
	{
		"idx" : 1355,
		"title" : "아트와떵",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/gZ0_eFVbd2CV",
		"status" : 1
	},
	{
		"idx" : 1356,
		"title" : "멜드 바이 기치조지",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/b_gNU4tCqinD",
		"status" : 1
	},
	{
		"idx" : 1357,
		"title" : "쿠시파파",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/e_uWh0gkespb",
		"status" : 1
	},
	{
		"idx" : 1358,
		"title" : "오레노라멘",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/s6C_cdBQX0rj",
		"status" : 1
	},
	{
		"idx" : 1359,
		"title" : "진만두",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/tCV5CXuBYX",
		"status" : 1
	},
	{
		"idx" : 1360,
		"title" : "산울림1992",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/kduafZiXUT",
		"status" : 1
	},
	{
		"idx" : 1361,
		"title" : "소금집델리 망원",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/_d9cArzpXEVI",
		"status" : 1
	},
	{
		"idx" : 1362,
		"title" : "당도",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/0my2hMzHlOYD",
		"status" : 1
	},
	{
		"idx" : 1363,
		"title" : "쿠이신보",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/mIomHshZmH",
		"status" : 1
	},
	{
		"idx" : 1364,
		"title" : "리틀빅토리",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/SyqlfkKhlAD0",
		"status" : 1
	},
	{
		"idx" : 1365,
		"title" : "토파",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/yYnRdrw-73XG",
		"status" : 1
	},
	{
		"idx" : 1366,
		"title" : "이치류",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/YqO915KDI9",
		"status" : 1
	},
	{
		"idx" : 1367,
		"title" : "키오스크",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/zOOlz9vfJfFF",
		"status" : 1
	},
	{
		"idx" : 1368,
		"title" : "멘야준",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/FlLnM4E0CUuz",
		"status" : 1
	},
	{
		"idx" : 1369,
		"title" : "코바시",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/bsAW30JU_zKX",
		"status" : 1
	},
	{
		"idx" : 1370,
		"title" : "산동만두",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/gLlD4v7E13",
		"status" : 1
	},
	{
		"idx" : 1371,
		"title" : "오츠커피",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/c6Wpmzll-0sN",
		"status" : 1
	},
	{
		"idx" : 1372,
		"title" : "하나라멘",
		"score" : "4.5",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/JOHRo9QUDRdi",
		"status" : 1
	},
	{
		"idx" : 1373,
		"title" : "피에트라",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/NXioT2lvlIi9",
		"status" : 1
	},
	{
		"idx" : 1374,
		"title" : "쉐시몽",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/NMCkZU9kduwC",
		"status" : 1
	},
	{
		"idx" : 1375,
		"title" : "은하루",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/vRjc_JKA-oDW",
		"status" : 1
	},
	{
		"idx" : 1376,
		"title" : "파이리퍼블릭",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/DB-nxyYhQbEJ",
		"status" : 1
	},
	{
		"idx" : 1377,
		"title" : "프롬하노이",
		"score" : "4.6",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/eHq8npkKK5dN",
		"status" : 1
	},
	{
		"idx" : 1378,
		"title" : "잘란연남",
		"score" : "4.4",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/W2pK3WhVFphk",
		"status" : 1
	},
	{
		"idx" : 1379,
		"title" : "프릳츠커피컴퍼니",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/lJTpl10oBA",
		"status" : 1
	},
	{
		"idx" : 1380,
		"title" : "오스테리아샘킴",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/aE9sGHedGUlj",
		"status" : 1
	},
	{
		"idx" : 1381,
		"title" : "중화복춘",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/UgFHZZczFUX-",
		"status" : 1
	},
	{
		"idx" : 1382,
		"title" : "잇텐고",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/sSnnhR-dDdqz",
		"status" : 1
	},
	{
		"idx" : 1383,
		"title" : "아날로그가든",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/bs2wK46E3R",
		"status" : 1
	},
	{
		"idx" : 1384,
		"title" : "미완성식탁",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/8bXvvebEbTRq",
		"status" : 1
	},
	{
		"idx" : 1385,
		"title" : "옥동식",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/2J0axpUplhy7",
		"status" : 1
	},
	{
		"idx" : 1386,
		"title" : "포비",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/Hrii5HjHIRoi",
		"status" : 1
	},
	{
		"idx" : 1387,
		"title" : "야키토리묵",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/bFIGUpV1xrg0",
		"status" : 1
	},
	{
		"idx" : 1388,
		"title" : "마시타야",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/ineF3MIAormc",
		"status" : 1
	},
	{
		"idx" : 1389,
		"title" : "라오삐약",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/B2Xej50-qhqL",
		"status" : 1
	},
	{
		"idx" : 1390,
		"title" : "연교",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/dHYMRd_-r-Ss",
		"status" : 1
	},
	{
		"idx" : 1391,
		"title" : "진진",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/YTeVoK0dx3",
		"status" : 1
	},
	{
		"idx" : 1392,
		"title" : "어반플랜트",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/-LWflJV1maU2",
		"status" : 1
	},
	{
		"idx" : 1393,
		"title" : "테일러커피",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/o3LQKSkc78",
		"status" : 1
	},
	{
		"idx" : 1394,
		"title" : "바다회사랑",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/u7hE5GfhEz",
		"status" : 1
	},
	{
		"idx" : 1395,
		"title" : "망원동즉석우동",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/kw9JM_fDCE",
		"status" : 1
	},
	{
		"idx" : 1396,
		"title" : "앤트러사이트",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/aG9jrSQ4UnRc",
		"status" : 1
	},
	{
		"idx" : 1397,
		"title" : "함반",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/9WduVohnusUp",
		"status" : 1
	},
	{
		"idx" : 1398,
		"title" : "멘지라멘",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/yLTZKyA_ro1v",
		"status" : 1
	},
	{
		"idx" : 1399,
		"title" : "바다회사랑",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/ox9K4mJOWf",
		"status" : 1
	},
	{
		"idx" : 1400,
		"title" : "우리바다수산",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/gmyDL4cBh9",
		"status" : 1
	},
	{
		"idx" : 1401,
		"title" : "평안도상원냉면",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/9VLsn_7CfpNv",
		"status" : 1
	},
	{
		"idx" : 1402,
		"title" : "이리에라멘",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/xeVvmrToKrul",
		"status" : 1
	},
	{
		"idx" : 1403,
		"title" : "양송이식당",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/myZSkYc9URUJ",
		"status" : 1
	},
	{
		"idx" : 1404,
		"title" : "젤라떼리아 에따",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/ic1srr8j1-SX",
		"status" : 1
	},
	{
		"idx" : 1405,
		"title" : "램랜드",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/PmeqDEWbEU",
		"status" : 1
	},
	{
		"idx" : 1406,
		"title" : "정정",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/L2JqAH9TQ7FQ",
		"status" : 1
	},
	{
		"idx" : 1407,
		"title" : "수부니흐",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/r9Ls1wRKf6-c",
		"status" : 1
	},
	{
		"idx" : 1408,
		"title" : "이박사의 신동막걸리",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/CMKn6mvsvqzW",
		"status" : 1
	},
	{
		"idx" : 1409,
		"title" : "아키야라멘",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/uNynTVBxuBBK",
		"status" : 1
	},
	{
		"idx" : 1410,
		"title" : "정든그릇",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/F9Af36AUr372",
		"status" : 1
	},
	{
		"idx" : 1411,
		"title" : "오마",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/1xTYoyKjDzRY",
		"status" : 1
	},
	{
		"idx" : 1412,
		"title" : "칸다소바",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/jMyukh-Vkuo3",
		"status" : 1
	},
	{
		"idx" : 1413,
		"title" : "돈까스광명",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/Ad2pgz7liZ7s",
		"status" : 1
	},
	{
		"idx" : 1414,
		"title" : "이와나시",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/xnnyUhC4HxCF",
		"status" : 1
	},
	{
		"idx" : 1415,
		"title" : "장작집",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/Eu4M-LuotC93",
		"status" : 1
	},
	{
		"idx" : 1416,
		"title" : "와이키키마켓",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/0zRLVVRjjEv8",
		"status" : 1
	},
	{
		"idx" : 1417,
		"title" : "여명",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/qh4LFFsUfh",
		"status" : 1
	},
	{
		"idx" : 1418,
		"title" : "세상끝의라멘",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/DM4Mb4dG1niW",
		"status" : 1
	},
	{
		"idx" : 1419,
		"title" : "우마담",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/sF8MmsuFBfg7",
		"status" : 1
	},
	{
		"idx" : 1420,
		"title" : "오헨",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/9mESyIiIe8UB",
		"status" : 1
	},
	{
		"idx" : 1421,
		"title" : "이요이요스시",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/QJH59JGDLYXj",
		"status" : 1
	},
	{
		"idx" : 1422,
		"title" : "지로우라멘",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/qTVR50wESV",
		"status" : 1
	},
	{
		"idx" : 1423,
		"title" : "카카오다다",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/X1wf0zACW32q",
		"status" : 1
	},
	{
		"idx" : 1424,
		"title" : "녹기전에",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/4PnxfuVSi_-z",
		"status" : 1
	},
	{
		"idx" : 1425,
		"title" : "야키토리 미식서울",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/kltj_ughTNJD",
		"status" : 1
	},
	{
		"idx" : 1426,
		"title" : "코코시에나 티오마카세",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/SsqRXVk2pbBu",
		"status" : 1
	},
	{
		"idx" : 1427,
		"title" : "조용한저녁",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/t3yUlEFTUg",
		"status" : 1
	},
	{
		"idx" : 1428,
		"title" : "리플레토레",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/vkM9QJRec2Fw",
		"status" : 1
	},
	{
		"idx" : 1429,
		"title" : "스아게 K",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/RLf-7Qchkwdk",
		"status" : 1
	},
	{
		"idx" : 1430,
		"title" : "당인동국수공장",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/v7MXLLwyuYVs",
		"status" : 1
	},
	{
		"idx" : 1431,
		"title" : "우노네",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/BLssczM1eL5d",
		"status" : 1
	},
	{
		"idx" : 1432,
		"title" : "더리얼치즈버거",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/UjLnh5W88htA",
		"status" : 1
	},
	{
		"idx" : 1433,
		"title" : "상해소흘",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/LmFShKuPK9Mz",
		"status" : 1
	},
	{
		"idx" : 1434,
		"title" : "아각아각",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/mPnubftPEx-J",
		"status" : 1
	},
	{
		"idx" : 1435,
		"title" : "온돈부리",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/1PGmuIVmvbW5",
		"status" : 1
	},
	{
		"idx" : 1436,
		"title" : "수을관",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/NmNhGW41EPD2",
		"status" : 1
	},
	{
		"idx" : 1437,
		"title" : "우이락",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/0o3xSbZoPv_C",
		"status" : 1
	},
	{
		"idx" : 1438,
		"title" : "스시미야비",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/eif8L-wpPmVQ",
		"status" : 1
	},
	{
		"idx" : 1439,
		"title" : "스시겐",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/IPJP_XU4cb",
		"status" : 1
	},
	{
		"idx" : 1440,
		"title" : "옥정",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/dIuYk5_dqa2k",
		"status" : 1
	},
	{
		"idx" : 1441,
		"title" : "정성",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/F0VINKyF1tLv",
		"status" : 1
	},
	{
		"idx" : 1442,
		"title" : "포포브레드",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/GTLov74hXWy1",
		"status" : 1
	},
	{
		"idx" : 1443,
		"title" : "청춘구락부",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/v0w6VUn4bi",
		"status" : 1
	},
	{
		"idx" : 1444,
		"title" : "커퍼시티",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/8t_RfEwtBKuJ",
		"status" : 1
	},
	{
		"idx" : 1445,
		"title" : "일등식당",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/_qloRj-hMz",
		"status" : 1
	},
	{
		"idx" : 1446,
		"title" : "연남화로",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/0NqIouMEtQES",
		"status" : 1
	},
	{
		"idx" : 1447,
		"title" : "루시드",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/DlaNVuhOXiQu",
		"status" : 1
	},
	{
		"idx" : 1448,
		"title" : "합정순대국",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/MIHsGjGadn",
		"status" : 1
	},
	{
		"idx" : 1449,
		"title" : "1989버거스탠드",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/xf3XMNYLEt2-",
		"status" : 1
	},
	{
		"idx" : 1450,
		"title" : "히트커피로스터스",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/jVlQ6xlMBLNc",
		"status" : 1
	},
	{
		"idx" : 1451,
		"title" : "핑크솔트 숯불구이",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/sU4kTZ4VwLQZ",
		"status" : 1
	},
	{
		"idx" : 1452,
		"title" : "커츠",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/WfglnIWt0xLx",
		"status" : 1
	},
	{
		"idx" : 1453,
		"title" : "테이커테이블",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/-y5tBsJqWfd3",
		"status" : 1
	},
	{
		"idx" : 1454,
		"title" : "웻핑거치즈스테이크",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/xecMNVgDAVNZ",
		"status" : 1
	},
	{
		"idx" : 1455,
		"title" : "영광보쌈",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/gKS2FVY_NB",
		"status" : 1
	},
	{
		"idx" : 1456,
		"title" : "미필담",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/mnMqrvEKJaXS",
		"status" : 1
	},
	{
		"idx" : 1457,
		"title" : "타오마라탕",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/n3vGElRYzNk9",
		"status" : 1
	},
	{
		"idx" : 1458,
		"title" : "저스티나",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/VOpLDlWL0CD0",
		"status" : 1
	},
	{
		"idx" : 1459,
		"title" : "웨스트빌피자",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/eH4IRRxr371x",
		"status" : 1
	},
	{
		"idx" : 1460,
		"title" : "둥둥막창구이",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/gjWlwujdy7WN",
		"status" : 1
	},
	{
		"idx" : 1461,
		"title" : "매일스시횟집",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/ChpR6-giTWcz",
		"status" : 1
	},
	{
		"idx" : 1462,
		"title" : "원조신촌설렁탕",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/UQ8pwjTnnKaE",
		"status" : 1
	},
	{
		"idx" : 1463,
		"title" : "산청엔흑돼지",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/_WHVHxNrKD_M",
		"status" : 1
	},
	{
		"idx" : 1464,
		"title" : "포멜로빈",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/irtCvPJoPgWI",
		"status" : 1
	},
	{
		"idx" : 1465,
		"title" : "연남제비",
		"score" : "4.3",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/alXMs5iWVPRZ",
		"status" : 1
	},
	{
		"idx" : 1466,
		"title" : "크레이지카츠",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/K1X3DD-Yr_2w",
		"status" : 1
	},
	{
		"idx" : 1467,
		"title" : "맛이차이나",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/TNywLOfH_r",
		"status" : 1
	},
	{
		"idx" : 1468,
		"title" : "을밀대",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/S15BRAV_W3",
		"status" : 1
	},
	{
		"idx" : 1469,
		"title" : "이요이요스시",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/Thi7FYrxzA",
		"status" : 1
	},
	{
		"idx" : 1470,
		"title" : "이치젠",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/Hois6uLTHet7",
		"status" : 1
	},
	{
		"idx" : 1471,
		"title" : "버터밀크",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/2OX3qazGeA",
		"status" : 1
	},
	{
		"idx" : 1472,
		"title" : "사루카메",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/NWBNy0tRqkUG",
		"status" : 1
	},
	{
		"idx" : 1473,
		"title" : "쥬마뺄",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/d6QJNyRAeUhU",
		"status" : 1
	},
	{
		"idx" : 1474,
		"title" : "커피가게동경",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/5jpxtJNIYu",
		"status" : 1
	},
	{
		"idx" : 1475,
		"title" : "요코쵸",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/FLRcNocF07CY",
		"status" : 1
	},
	{
		"idx" : 1476,
		"title" : "카밀로 라자네리아",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/kDfUb7VzjEtZ",
		"status" : 1
	},
	{
		"idx" : 1477,
		"title" : "하하",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/C75jwQNhWx",
		"status" : 1
	},
	{
		"idx" : 1478,
		"title" : "커피하우스마이샤",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/HjOheVGZ6Ndh",
		"status" : 1
	},
	{
		"idx" : 1479,
		"title" : "과자산책",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/S1KQU7hwpSWU",
		"status" : 1
	},
	{
		"idx" : 1480,
		"title" : "덕이손만두",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/UzUVsCM4Nr",
		"status" : 1
	},
	{
		"idx" : 1481,
		"title" : "에이든",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/cYjBEzJOJxvR",
		"status" : 1
	},
	{
		"idx" : 1482,
		"title" : "야경",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/HRy6f8zeqbjH",
		"status" : 1
	},
	{
		"idx" : 1483,
		"title" : "계고기집",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/iTAe3KwUXvJU",
		"status" : 1
	},
	{
		"idx" : 1484,
		"title" : "청기와타운",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/ZIwnKQaQDi9p",
		"status" : 1
	},
	{
		"idx" : 1485,
		"title" : "온정",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/LMC_eb29aE68",
		"status" : 1
	},
	{
		"idx" : 1486,
		"title" : "달고나",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/ZsM2PnBd9RKp",
		"status" : 1
	},
	{
		"idx" : 1487,
		"title" : "흠식당",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/oXx1siXaX_3m",
		"status" : 1
	},
	{
		"idx" : 1488,
		"title" : "제로햄",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/XOts5rcD_YSe",
		"status" : 1
	},
	{
		"idx" : 1489,
		"title" : "로쏘1924",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/ls948dutYgsg",
		"status" : 1
	},
	{
		"idx" : 1490,
		"title" : "힠컵",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/d5sqHw5xPQWk",
		"status" : 1
	},
	{
		"idx" : 1491,
		"title" : "카츠닉",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/V7EeY6YeZtQf",
		"status" : 1
	},
	{
		"idx" : 1492,
		"title" : "물고기초밥",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/2tpS8RsBab",
		"status" : 1
	},
	{
		"idx" : 1493,
		"title" : "어라운드 그린",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/ZVhFoj2Ly_8D",
		"status" : 1
	},
	{
		"idx" : 1494,
		"title" : "고시고시",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/sbvSo2QkfA5q",
		"status" : 1
	},
	{
		"idx" : 1495,
		"title" : "스시지현",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/3MLBJ-6DeznK",
		"status" : 1
	},
	{
		"idx" : 1496,
		"title" : "바이러닉에스프레소바",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/b7cL4tnzZlHK",
		"status" : 1
	},
	{
		"idx" : 1497,
		"title" : "류",
		"score" : "4.2",
		"region" : "마포구",
		"url" : "https://www.mangoplate.com/restaurants/GpFSFEeSQT",
		"status" : 1
	},
	{
		"idx" : 1498,
		"title" : "잭슨피자",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/L34goxmpX0kv",
		"status" : 1
	},
	{
		"idx" : 1499,
		"title" : "춈",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/2VDMQwhlARr_",
		"status" : 1
	},
	{
		"idx" : 1500,
		"title" : "힐즈앤유로파",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/ybArAanW5EhS",
		"status" : 1
	},
	{
		"idx" : 1501,
		"title" : "성월동화",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/4LBHf3T2ZXzN",
		"status" : 1
	},
	{
		"idx" : 1502,
		"title" : "비일",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/b101h_jwBNCJ",
		"status" : 1
	},
	{
		"idx" : 1503,
		"title" : "다운타우너",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/y-_XMRSTNrAi",
		"status" : 1
	},
	{
		"idx" : 1504,
		"title" : "바토스",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/O2hjKOgn9E",
		"status" : 1
	},
	{
		"idx" : 1505,
		"title" : "매니멀스모크하우스",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/71KcF_LODj",
		"status" : 1
	},
	{
		"idx" : 1506,
		"title" : "호머피자",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/SqI7JhOCrH9A",
		"status" : 1
	},
	{
		"idx" : 1507,
		"title" : "우스블랑",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/3QUGIFzva0",
		"status" : 1
	},
	{
		"idx" : 1508,
		"title" : "코레아노스키친",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/UBDoQXw6-C",
		"status" : 1
	},
	{
		"idx" : 1509,
		"title" : "다츠",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/uEWpasDGgu6t",
		"status" : 1
	},
	{
		"idx" : 1510,
		"title" : "지노스뉴욕피자",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/vaSEEQafFwKF",
		"status" : 1
	},
	{
		"idx" : 1511,
		"title" : "카사블랑카",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/6xQY0t3A6o",
		"status" : 1
	},
	{
		"idx" : 1512,
		"title" : "모수",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/eAJYfITosHjc",
		"status" : 1
	},
	{
		"idx" : 1513,
		"title" : "꺼거",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/TKb98SN3qdOr",
		"status" : 1
	},
	{
		"idx" : 1514,
		"title" : "페트라",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/n9ZwosnPSP",
		"status" : 1
	},
	{
		"idx" : 1515,
		"title" : "써머레인",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/1B8ARZ_X2Wur",
		"status" : 1
	},
	{
		"idx" : 1516,
		"title" : "모로코코 카페",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/Xn6RcdfFQu5s",
		"status" : 1
	},
	{
		"idx" : 1517,
		"title" : "오근내 닭갈비",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/0thCFqf_UT",
		"status" : 1
	},
	{
		"idx" : 1518,
		"title" : "시칠리",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/xVrzTHTEMVpI",
		"status" : 1
	},
	{
		"idx" : 1519,
		"title" : "알레즈",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/NoGCorBVkjwi",
		"status" : 1
	},
	{
		"idx" : 1520,
		"title" : "더티스낵",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/EkiCy9d8fAg8",
		"status" : 1
	},
	{
		"idx" : 1521,
		"title" : "라따뚜이인서울",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/jqrB6Jv2RTUB",
		"status" : 1
	},
	{
		"idx" : 1522,
		"title" : "미타스",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/rMtFLYZbemk9",
		"status" : 1
	},
	{
		"idx" : 1523,
		"title" : "넘버원양꼬치훠궈",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/a0AW4LfEbjSs",
		"status" : 1
	},
	{
		"idx" : 1524,
		"title" : "용산양다리",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/tZ5rbp5jBT7B",
		"status" : 1
	},
	{
		"idx" : 1525,
		"title" : "바이두부",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/T8JmmKQ0hcD-",
		"status" : 1
	},
	{
		"idx" : 1526,
		"title" : "브라이리퍼블릭",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/F4LMucA69A",
		"status" : 1
	},
	{
		"idx" : 1527,
		"title" : "르페셰미뇽",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/rGU39IqaaEHz",
		"status" : 1
	},
	{
		"idx" : 1528,
		"title" : "야상해",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/PSgsnTisSpxC",
		"status" : 1
	},
	{
		"idx" : 1529,
		"title" : "남영돈",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/EKqwrA1KDZ5c",
		"status" : 1
	},
	{
		"idx" : 1530,
		"title" : "카밀로한남",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/dLdUO7EluIG5",
		"status" : 1
	},
	{
		"idx" : 1531,
		"title" : "샐러드셀러",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/pWBiN0PLlB",
		"status" : 1
	},
	{
		"idx" : 1532,
		"title" : "디템포레",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/3RT5ty2NgR5g",
		"status" : 1
	},
	{
		"idx" : 1533,
		"title" : "뮤땅",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/N6VvLFu0C4Zk",
		"status" : 1
	},
	{
		"idx" : 1534,
		"title" : "꾸잉",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/MlYlQwcNxHL3",
		"status" : 1
	},
	{
		"idx" : 1535,
		"title" : "캘리포니아키친앤크래프트펍",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/aMvqo8Ypz2yP",
		"status" : 1
	},
	{
		"idx" : 1536,
		"title" : "해방촌 노아",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/0Ml4Wl9ZTv",
		"status" : 1
	},
	{
		"idx" : 1537,
		"title" : "남박",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/gczaSZvc3W5b",
		"status" : 1
	},
	{
		"idx" : 1538,
		"title" : "하쿠시",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/NUqGz0WrOowF",
		"status" : 1
	},
	{
		"idx" : 1539,
		"title" : "FOURB",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/CJKTHzGOCQi9",
		"status" : 1
	},
	{
		"idx" : 1540,
		"title" : "세몰리나클럽",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/NtrLO5KqplMX",
		"status" : 1
	},
	{
		"idx" : 1541,
		"title" : "푸에고",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/CW2epvH_igAG",
		"status" : 1
	},
	{
		"idx" : 1542,
		"title" : "주파카",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/KsI715UsGtV0",
		"status" : 1
	},
	{
		"idx" : 1543,
		"title" : "바우카페",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/rSo9uQOd8RmJ",
		"status" : 1
	},
	{
		"idx" : 1544,
		"title" : "치로피자바",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/d2p5CX8PIsde",
		"status" : 1
	},
	{
		"idx" : 1545,
		"title" : "야끼니꾸소량 (휴업중)",
		"score" : "4.5",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/2ui-zlCn2VvH",
		"status" : 1
	},
	{
		"idx" : 1546,
		"title" : "보니스피자펍",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/gL8RksQTNk",
		"status" : 1
	},
	{
		"idx" : 1547,
		"title" : "롸카두들내쉬빌핫치킨",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/iqRglQ9mvs89",
		"status" : 1
	},
	{
		"idx" : 1548,
		"title" : "하시엔다",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/p0wRvl72l2",
		"status" : 1
	},
	{
		"idx" : 1549,
		"title" : "매덕스피자",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/2NG2Ehby9t",
		"status" : 1
	},
	{
		"idx" : 1550,
		"title" : "파이프그라운드",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/qcFPjfB7o5-X",
		"status" : 1
	},
	{
		"idx" : 1551,
		"title" : "라구",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/-1yzcgbtF5",
		"status" : 1
	},
	{
		"idx" : 1552,
		"title" : "네키드윙즈",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/RUAaH7p5m8c_",
		"status" : 1
	},
	{
		"idx" : 1553,
		"title" : "제이엘 디저트바",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/O1EySl2Zq7TE",
		"status" : 1
	},
	{
		"idx" : 1554,
		"title" : "시멘트",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/l45tGeIE-JPk",
		"status" : 1
	},
	{
		"idx" : 1555,
		"title" : "재인",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/ZpyE9jWyOKcp",
		"status" : 1
	},
	{
		"idx" : 1556,
		"title" : "오츠커피",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/9lwUASfsAqk2",
		"status" : 1
	},
	{
		"idx" : 1557,
		"title" : "반창고",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/pY-2R3zbaCaF",
		"status" : 1
	},
	{
		"idx" : 1558,
		"title" : "한남동한방통닭",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/NyDbhBM5mv",
		"status" : 1
	},
	{
		"idx" : 1559,
		"title" : "박소린두깜풍",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/3YYUsJQb0eAY",
		"status" : 1
	},
	{
		"idx" : 1560,
		"title" : "팟카파우",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/esOzAbY-3iUK",
		"status" : 1
	},
	{
		"idx" : 1561,
		"title" : "바마셀",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/kHHKj3majCAO",
		"status" : 1
	},
	{
		"idx" : 1562,
		"title" : "방방",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/ET4FsCWAC-un",
		"status" : 1
	},
	{
		"idx" : 1563,
		"title" : "부산복국 고래고기",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/aBun6cmMGmqk",
		"status" : 1
	},
	{
		"idx" : 1564,
		"title" : "뷔봉",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/49oZZCEg0sw4",
		"status" : 1
	},
	{
		"idx" : 1565,
		"title" : "더백테라스",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/lPM5ZHvbKiSI",
		"status" : 1
	},
	{
		"idx" : 1566,
		"title" : "콘디토리오븐",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/bP5TivKxMwwC",
		"status" : 1
	},
	{
		"idx" : 1567,
		"title" : "한우물",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/7FsLyC-UAaT2",
		"status" : 1
	},
	{
		"idx" : 1568,
		"title" : "코지빌라커피",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/5pYPUF2b4YR5",
		"status" : 1
	},
	{
		"idx" : 1569,
		"title" : "미트로칼",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/WiAaloLq8GpW",
		"status" : 1
	},
	{
		"idx" : 1570,
		"title" : "디브루잉",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/teEfIJyX2Q1z",
		"status" : 1
	},
	{
		"idx" : 1571,
		"title" : "용산양꼬치",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/U0uLxCJB1xUW",
		"status" : 1
	},
	{
		"idx" : 1572,
		"title" : "섬집",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/Hd4gpYLlhy",
		"status" : 1
	},
	{
		"idx" : 1573,
		"title" : "락희",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/rSAQbVIdneem",
		"status" : 1
	},
	{
		"idx" : 1574,
		"title" : "야키니쿠소문",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/m1UcTO-ZwcGN",
		"status" : 1
	},
	{
		"idx" : 1575,
		"title" : "능동미나리",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/gfwn3SvGRI3i",
		"status" : 1
	},
	{
		"idx" : 1576,
		"title" : "식캣사인",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/1wwENyLcLAg4",
		"status" : 1
	},
	{
		"idx" : 1577,
		"title" : "한길포장마차",
		"score" : "4.4",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/xov_RaVGvV46",
		"status" : 1
	},
	{
		"idx" : 1578,
		"title" : "판코네",
		"score" : "4.8",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/tVGs0x42pLKv",
		"status" : 1
	},
	{
		"idx" : 1579,
		"title" : "치즈플로",
		"score" : "4.8",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/-tjn7yYAEu7u",
		"status" : 1
	},
	{
		"idx" : 1580,
		"title" : "크리스피포크타운",
		"score" : "4.8",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/_7MTHsDE7UXc",
		"status" : 1
	},
	{
		"idx" : 1581,
		"title" : "양인환대극진",
		"score" : "4.7",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/1S_zWk5BW7Fd",
		"status" : 1
	},
	{
		"idx" : 1582,
		"title" : "바위파스타바",
		"score" : "4.7",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/0ZBL14x1k0Re",
		"status" : 1
	},
	{
		"idx" : 1583,
		"title" : "서울케밥",
		"score" : "4.7",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/n3DOag6F8BPe",
		"status" : 1
	},
	{
		"idx" : 1584,
		"title" : "조이스팔라펠",
		"score" : "4.7",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/6CZwyyCzr6qI",
		"status" : 1
	},
	{
		"idx" : 1585,
		"title" : "카카오봄",
		"score" : "4.7",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/QqeR-5G5uWnd",
		"status" : 1
	},
	{
		"idx" : 1586,
		"title" : "내추럴하이",
		"score" : "4.7",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/WvYz0dZzXyX7",
		"status" : 1
	},
	{
		"idx" : 1587,
		"title" : "화양연가",
		"score" : "4.7",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/ECgCJHThGX",
		"status" : 1
	},
	{
		"idx" : 1588,
		"title" : "세스타",
		"score" : "4.7",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/8RcvjM6aCNCP",
		"status" : 1
	},
	{
		"idx" : 1589,
		"title" : "야키토리혼바",
		"score" : "4.7",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/ZTR5cHoo-bYA",
		"status" : 1
	},
	{
		"idx" : 1590,
		"title" : "쥬에",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/Fvgyq1HAiny6",
		"status" : 1
	},
	{
		"idx" : 1591,
		"title" : "오스테리아 오르조",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/S-nogDkD8F83",
		"status" : 1
	},
	{
		"idx" : 1592,
		"title" : "오제제",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/mzUvz-k-0Szd",
		"status" : 1
	},
	{
		"idx" : 1593,
		"title" : "레에스티우",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/zq9bIKh6PMLV",
		"status" : 1
	},
	{
		"idx" : 1594,
		"title" : "야스노야지로",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/9rXplW6ajjWI",
		"status" : 1
	},
	{
		"idx" : 1595,
		"title" : "포카치아델라스트라다",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/1YOKBfjGS7LU",
		"status" : 1
	},
	{
		"idx" : 1596,
		"title" : "양인환대 정인",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/aGO25PgN0-Zg",
		"status" : 1
	},
	{
		"idx" : 1597,
		"title" : "북천",
		"score" : "4.6",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/iXobcHXQf6",
		"status" : 1
	},
	{
		"idx" : 1598,
		"title" : "끌레망꾸꾸",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/O1k4pqtp3CZo",
		"status" : 1
	},
	{
		"idx" : 1599,
		"title" : "산수화",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/jschADggh-",
		"status" : 1
	},
	{
		"idx" : 1600,
		"title" : "당스",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/fLDxEycDdioq",
		"status" : 1
	},
	{
		"idx" : 1601,
		"title" : "24시뼈다귀감자탕",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/mcj4cd4eQf",
		"status" : 1
	},
	{
		"idx" : 1602,
		"title" : "쌍대포",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/rJhG2_tI_H",
		"status" : 1
	},
	{
		"idx" : 1603,
		"title" : "카페손",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/_y-r0-m3RNYj",
		"status" : 1
	},
	{
		"idx" : 1604,
		"title" : "손문 대구막창 갈매기살",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/a7Gx4WM0xe",
		"status" : 1
	},
	{
		"idx" : 1605,
		"title" : "가타부타",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/wZPn3Plo6dsZ",
		"status" : 1
	},
	{
		"idx" : 1606,
		"title" : "인소울",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/V3GNiu3Z-0Ni",
		"status" : 1
	},
	{
		"idx" : 1607,
		"title" : "팻캣",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/wnDQacLgqe",
		"status" : 1
	},
	{
		"idx" : 1608,
		"title" : "사랑방참숯화로구이",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/5W_oXN_QyP1w",
		"status" : 1
	},
	{
		"idx" : 1609,
		"title" : "청기와타운",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/_1eF278T-P_L",
		"status" : 1
	},
	{
		"idx" : 1610,
		"title" : "와인집",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/zoFsSqdowt3z",
		"status" : 1
	},
	{
		"idx" : 1611,
		"title" : "쿠로이야",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/pPLQLdhIt3SK",
		"status" : 1
	},
	{
		"idx" : 1612,
		"title" : "데칼코마니",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/Lm2FqcQtnx1d",
		"status" : 1
	},
	{
		"idx" : 1613,
		"title" : "심퍼티쿠시",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/yGsWbkgRsDjm",
		"status" : 1
	},
	{
		"idx" : 1614,
		"title" : "서울역철도떡볶이",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/LZ-WPodVBd9N",
		"status" : 1
	},
	{
		"idx" : 1615,
		"title" : "부산어묵",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/_aP_V4ZMNBJQ",
		"status" : 1
	},
	{
		"idx" : 1616,
		"title" : "해방촌닭",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/e9ecscZZE5-v",
		"status" : 1
	},
	{
		"idx" : 1617,
		"title" : "해방식당",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/sKZzSdMtSONG",
		"status" : 1
	},
	{
		"idx" : 1618,
		"title" : "비스트로 루틴",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/QykyLMvPsg",
		"status" : 1
	},
	{
		"idx" : 1619,
		"title" : "초원",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/LkuUboV73Gpp",
		"status" : 1
	},
	{
		"idx" : 1620,
		"title" : "오월의종",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/zNVXE1__XF",
		"status" : 1
	},
	{
		"idx" : 1621,
		"title" : "오파토",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/wgLcFMiJ0pEc",
		"status" : 1
	},
	{
		"idx" : 1622,
		"title" : "한냄비",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/0sdpvAeUeb18",
		"status" : 1
	},
	{
		"idx" : 1623,
		"title" : "테판",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/ky2mMIz5at2z",
		"status" : 1
	},
	{
		"idx" : 1624,
		"title" : "몽크스부처",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/GN9VBv4DEGlr",
		"status" : 1
	},
	{
		"idx" : 1625,
		"title" : "부첼리하우스",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/-xPVTErx1_zS",
		"status" : 1
	},
	{
		"idx" : 1626,
		"title" : "트로이카",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/wKCH7UiJm5RQ",
		"status" : 1
	},
	{
		"idx" : 1627,
		"title" : "우라만",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/9TtK_cdvAJV6",
		"status" : 1
	},
	{
		"idx" : 1628,
		"title" : "조대포",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/8c_tpZgCYB",
		"status" : 1
	},
	{
		"idx" : 1629,
		"title" : "양인환대",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/-KstCZj7GoFn",
		"status" : 1
	},
	{
		"idx" : 1630,
		"title" : "타카",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/AhYygBstL4Ov",
		"status" : 1
	},
	{
		"idx" : 1631,
		"title" : "PPS",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/64qKVf_0O512",
		"status" : 1
	},
	{
		"idx" : 1632,
		"title" : "스시이젠",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/nS1JAcY5Pjs0",
		"status" : 1
	},
	{
		"idx" : 1633,
		"title" : "베이커리무이",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/_czAygB7d4kj",
		"status" : 1
	},
	{
		"idx" : 1634,
		"title" : "REVEAT",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/7j-gLbV91mc5",
		"status" : 1
	},
	{
		"idx" : 1635,
		"title" : "한와담블랙",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/Xy2DIpxdFd",
		"status" : 1
	},
	{
		"idx" : 1636,
		"title" : "KEEM HANNAM",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/VecthKr8eQJ8",
		"status" : 1
	},
	{
		"idx" : 1637,
		"title" : "오근내2닭갈비",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/bHVJz_hK9s",
		"status" : 1
	},
	{
		"idx" : 1638,
		"title" : "아티장베이커스",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/8mhsdtiBg0",
		"status" : 1
	},
	{
		"idx" : 1639,
		"title" : "소울다이닝",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/Lj8LbMuvciWk",
		"status" : 1
	},
	{
		"idx" : 1640,
		"title" : "구찌 오스테리아 서울",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/lDXp0aoc1OQ3",
		"status" : 1
	},
	{
		"idx" : 1641,
		"title" : "어제의 카레",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/6yO8cPqu-Zhx",
		"status" : 1
	},
	{
		"idx" : 1642,
		"title" : "라비앙코코",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/nsH8vA5Gq0XW",
		"status" : 1
	},
	{
		"idx" : 1643,
		"title" : "끌라시끄",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/YlqhtvLZV8DS",
		"status" : 1
	},
	{
		"idx" : 1644,
		"title" : "누랑즈뉘",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/9y-8Nnf7jDyz",
		"status" : 1
	},
	{
		"idx" : 1645,
		"title" : "오띠젤리",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/1s5LFv7ObZXx",
		"status" : 1
	},
	{
		"idx" : 1646,
		"title" : "쎄니에",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/3p8J1JHs-FlW",
		"status" : 1
	},
	{
		"idx" : 1647,
		"title" : "부토",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/8DZNH8cpZ5yy",
		"status" : 1
	},
	{
		"idx" : 1648,
		"title" : "탄산바",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/1L-wM-1DU3Vv",
		"status" : 1
	},
	{
		"idx" : 1649,
		"title" : "효도치킨",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/iYXmuzgMI1uc",
		"status" : 1
	},
	{
		"idx" : 1650,
		"title" : "느루",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/wIyt2zrjT-gg",
		"status" : 1
	},
	{
		"idx" : 1651,
		"title" : "쿠촐로 서울",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/kguoyuEh3Fro",
		"status" : 1
	},
	{
		"idx" : 1652,
		"title" : "데일리루틴",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/J6zzI_764si0",
		"status" : 1
	},
	{
		"idx" : 1653,
		"title" : "덕순루",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/CJNrnL9ve3Ok",
		"status" : 1
	},
	{
		"idx" : 1654,
		"title" : "소꿉",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/jUCueap1rh",
		"status" : 1
	},
	{
		"idx" : 1655,
		"title" : "루",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/UsoUec1dJpq7",
		"status" : 1
	},
	{
		"idx" : 1656,
		"title" : "이태원소주집",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/fmTJWgXvp-T7",
		"status" : 1
	},
	{
		"idx" : 1657,
		"title" : "명동교자",
		"score" : "4.3",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/sG3FofldAJgm",
		"status" : 1
	},
	{
		"idx" : 1658,
		"title" : "몽탄",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/y5gP4BbLDHA8",
		"status" : 1
	},
	{
		"idx" : 1659,
		"title" : "라페름",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/k6tCnrg0Z6",
		"status" : 1
	},
	{
		"idx" : 1660,
		"title" : "뇨끼바 (휴업중)",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/AvMNYihI5m9f",
		"status" : 1
	},
	{
		"idx" : 1661,
		"title" : "플랜트",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/8GRQ6g5tH8GB",
		"status" : 1
	},
	{
		"idx" : 1662,
		"title" : "에그앤플라워",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/xPBKK3JjW7BC",
		"status" : 1
	},
	{
		"idx" : 1663,
		"title" : "챔프커피",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/wkaQCfkewJ",
		"status" : 1
	},
	{
		"idx" : 1664,
		"title" : "어프로치",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/SsjvfmOqcPy9",
		"status" : 1
	},
	{
		"idx" : 1665,
		"title" : "한입소반",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/C1EUU9PoZuIN",
		"status" : 1
	},
	{
		"idx" : 1666,
		"title" : "효뜨",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/A_ty1wPgIJQv",
		"status" : 1
	},
	{
		"idx" : 1667,
		"title" : "스즈란테이",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/F1cDuMPVaT",
		"status" : 1
	},
	{
		"idx" : 1668,
		"title" : "루트에브리데이",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/7A-UpyjiDuXH",
		"status" : 1
	},
	{
		"idx" : 1669,
		"title" : "한남작업실",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/mMH-BhYMMuFJ",
		"status" : 1
	},
	{
		"idx" : 1670,
		"title" : "맥심플랜트",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/yZeBZHkRPn0_",
		"status" : 1
	},
	{
		"idx" : 1671,
		"title" : "한국술집안씨막걸리",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/-5ZJ_ubniX",
		"status" : 1
	},
	{
		"idx" : 1672,
		"title" : "쿼츠커피",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/yr7Wrqa5_dqc",
		"status" : 1
	},
	{
		"idx" : 1673,
		"title" : "리틀넥 한남",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/ROSWsOFnCUXC",
		"status" : 1
	},
	{
		"idx" : 1674,
		"title" : "봉쥬르스고이",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/KPcw29bepdzi",
		"status" : 1
	},
	{
		"idx" : 1675,
		"title" : "문배동육칼",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/FDxrWxhxqd",
		"status" : 1
	},
	{
		"idx" : 1676,
		"title" : "쇼니노",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/fQoJSrarf7QR",
		"status" : 1
	},
	{
		"idx" : 1677,
		"title" : "로스트인홍콩",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/iKB0kCnJD_wL",
		"status" : 1
	},
	{
		"idx" : 1678,
		"title" : "중화객잔 수",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/LOtUmFfLi45q",
		"status" : 1
	},
	{
		"idx" : 1679,
		"title" : "물고기주택",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/L29qKbKIPn2Z",
		"status" : 1
	},
	{
		"idx" : 1680,
		"title" : "용산은행나무포차",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/pe9lh70Uu5li",
		"status" : 1
	},
	{
		"idx" : 1681,
		"title" : "모르페커피",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/Rj3v-Vkem1Vo",
		"status" : 1
	},
	{
		"idx" : 1682,
		"title" : "성광대도",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/AtIDE0eIN9ul",
		"status" : 1
	},
	{
		"idx" : 1683,
		"title" : "우사단고기",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/D9ymD6cfFjhl",
		"status" : 1
	},
	{
		"idx" : 1684,
		"title" : "이웃집영준이",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/YDYBTHkquPNf",
		"status" : 1
	},
	{
		"idx" : 1685,
		"title" : "고다이",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/qD9CIUd6zFOQ",
		"status" : 1
	},
	{
		"idx" : 1686,
		"title" : "당케커피",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/qP_cL7uib9hi",
		"status" : 1
	},
	{
		"idx" : 1687,
		"title" : "몬스터플레이스",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/FT6X0FrSqOx9",
		"status" : 1
	},
	{
		"idx" : 1688,
		"title" : "캄포",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/4R6ZEJ0_ywur",
		"status" : 1
	},
	{
		"idx" : 1689,
		"title" : "돈카츠팔월",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/cZ9qQ4Pw6RsS",
		"status" : 1
	},
	{
		"idx" : 1690,
		"title" : "하이타이",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/Hgtgmg5J8oit",
		"status" : 1
	},
	{
		"idx" : 1691,
		"title" : "피닉스 (휴업중)",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/66bUdgyLlubV",
		"status" : 1
	},
	{
		"idx" : 1692,
		"title" : "김종용누룽지통닭",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/wBGt4NzjE1Vy",
		"status" : 1
	},
	{
		"idx" : 1693,
		"title" : "트로이",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/iSauQK2nYoSe",
		"status" : 1
	},
	{
		"idx" : 1694,
		"title" : "한강집",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/j8uwJkVP0L",
		"status" : 1
	},
	{
		"idx" : 1695,
		"title" : "올딧세",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/Av5FzoYu_w9H",
		"status" : 1
	},
	{
		"idx" : 1696,
		"title" : "심야식당 기억",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/MLiMIMzQMV6w",
		"status" : 1
	},
	{
		"idx" : 1697,
		"title" : "소세지하우스",
		"score" : "4.2",
		"region" : "용산구",
		"url" : "https://www.mangoplate.com/restaurants/C_7F5tbGTbmW",
		"status" : 1
	},
	{
		"idx" : 1698,
		"title" : "마리오네",
		"score" : "4.8",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/e5avGLO5hjJM",
		"status" : 1
	},
	{
		"idx" : 1699,
		"title" : "지우관",
		"score" : "4.8",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/EI2Z304ave3h",
		"status" : 1
	},
	{
		"idx" : 1700,
		"title" : "미오도쿄다이닝",
		"score" : "4.7",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/bCF4FCZPy1Cs",
		"status" : 1
	},
	{
		"idx" : 1701,
		"title" : "디핀옥수",
		"score" : "4.7",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/AUBFvfRpvC4J",
		"status" : 1
	},
	{
		"idx" : 1702,
		"title" : "프롤라",
		"score" : "4.6",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/vCgSj_O_Xjy9",
		"status" : 1
	},
	{
		"idx" : 1703,
		"title" : "쿠나",
		"score" : "4.6",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/ldYYbW06oG1B",
		"status" : 1
	},
	{
		"idx" : 1704,
		"title" : "발렁스",
		"score" : "4.6",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/-lyoPbsT9s97",
		"status" : 1
	},
	{
		"idx" : 1705,
		"title" : "돈까스전원",
		"score" : "4.6",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/-csjvM0O5SlH",
		"status" : 1
	},
	{
		"idx" : 1706,
		"title" : "센서리커피로스터스",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/BpmqCj4fCNw1",
		"status" : 1
	},
	{
		"idx" : 1707,
		"title" : "한냄비",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/lgPqPZUtVrdv",
		"status" : 1
	},
	{
		"idx" : 1708,
		"title" : "라무라",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/IGCpbFt4EK_8",
		"status" : 1
	},
	{
		"idx" : 1709,
		"title" : "핫쵸",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/V1-abXB-vt2f",
		"status" : 1
	},
	{
		"idx" : 1710,
		"title" : "주052",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/sCZhvMG9Dzok",
		"status" : 1
	},
	{
		"idx" : 1711,
		"title" : "호감도",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/RFmo6vVoE6eS",
		"status" : 1
	},
	{
		"idx" : 1712,
		"title" : "보다버거",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/WD6vllKoaRJ5",
		"status" : 1
	},
	{
		"idx" : 1713,
		"title" : "그라데이션커피",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/3Cb2Gdky91sG",
		"status" : 1
	},
	{
		"idx" : 1714,
		"title" : "옥정김밥",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/WJw40i0jZZZZ",
		"status" : 1
	},
	{
		"idx" : 1715,
		"title" : "땅코참숯구이",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/pPeFnKHcfu",
		"status" : 1
	},
	{
		"idx" : 1716,
		"title" : "본앤브레드",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/AcH2FbCE4S19",
		"status" : 1
	},
	{
		"idx" : 1717,
		"title" : "소소하게",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Cx7vdBVpKIjM",
		"status" : 1
	},
	{
		"idx" : 1718,
		"title" : "팜티진쌀국수",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/jhTT8SeA2F",
		"status" : 1
	},
	{
		"idx" : 1719,
		"title" : "카린지 린가네 스낵바",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/L0NcQHUBkQpe",
		"status" : 1
	},
	{
		"idx" : 1720,
		"title" : "제이드앤워터",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/ZEPNM3jYfkyk",
		"status" : 1
	},
	{
		"idx" : 1721,
		"title" : "스시오오모토",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/O9b3wAbgCHJW",
		"status" : 1
	},
	{
		"idx" : 1722,
		"title" : "도렐",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/J-yKZJNQtePd",
		"status" : 1
	},
	{
		"idx" : 1723,
		"title" : "성수족발",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/nPulEWplLE",
		"status" : 1
	},
	{
		"idx" : 1724,
		"title" : "악어떡볶이",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/9uRzZUi47C",
		"status" : 1
	},
	{
		"idx" : 1725,
		"title" : "성수베이킹스튜디오",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/5LCFK_Iifbke",
		"status" : 1
	},
	{
		"idx" : 1726,
		"title" : "우오보파스타바",
		"score" : "4.6",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/2qFEx0pXrDdZ",
		"status" : 1
	},
	{
		"idx" : 1727,
		"title" : "높은산",
		"score" : "4.6",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/W9HA8CD1HJe7",
		"status" : 1
	},
	{
		"idx" : 1728,
		"title" : "세스크멘슬",
		"score" : "4.5",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/lBwwvWFhnPMp",
		"status" : 1
	},
	{
		"idx" : 1729,
		"title" : "우동가조쿠",
		"score" : "4.5",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/oArmwzCBGZ",
		"status" : 1
	},
	{
		"idx" : 1730,
		"title" : "성수 수집",
		"score" : "4.5",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/NUfBRt7o1nbd",
		"status" : 1
	},
	{
		"idx" : 1731,
		"title" : "시옹마오",
		"score" : "4.5",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Pga2wB_yA32d",
		"status" : 1
	},
	{
		"idx" : 1732,
		"title" : "에보",
		"score" : "4.5",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/b66fkZcBDHJN",
		"status" : 1
	},
	{
		"idx" : 1733,
		"title" : "다로베",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/ie3TAxVUoaZR",
		"status" : 1
	},
	{
		"idx" : 1734,
		"title" : "팩피",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/vAwCxHClYyxP",
		"status" : 1
	},
	{
		"idx" : 1735,
		"title" : "마하차이",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/KQI3uO4Kw1wn",
		"status" : 1
	},
	{
		"idx" : 1736,
		"title" : "르프리크",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/LMOnpDfa9HoA",
		"status" : 1
	},
	{
		"idx" : 1737,
		"title" : "누메로도스",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/joXmYQa1O6Rq",
		"status" : 1
	},
	{
		"idx" : 1738,
		"title" : "춘향미엔",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/7SS6-guzJWfm",
		"status" : 1
	},
	{
		"idx" : 1739,
		"title" : "차만다",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/8TEVbLAud8hP",
		"status" : 1
	},
	{
		"idx" : 1740,
		"title" : "로우커피스탠드",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/AHfFLHT86Lt4",
		"status" : 1
	},
	{
		"idx" : 1741,
		"title" : "누메로뜨레쓰",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/l4xy6mRsW0tK",
		"status" : 1
	},
	{
		"idx" : 1742,
		"title" : "당도",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/4qnCi8_87ger",
		"status" : 1
	},
	{
		"idx" : 1743,
		"title" : "가조쿠",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/MIK9Lf2GfH6B",
		"status" : 1
	},
	{
		"idx" : 1744,
		"title" : "소랑호젠",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/MWPiVInHLptk",
		"status" : 1
	},
	{
		"idx" : 1745,
		"title" : "유어네이키드치즈",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/wtVI5ndRldee",
		"status" : 1
	},
	{
		"idx" : 1746,
		"title" : "패티앤베지스",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/BS1HlLGkvCcc",
		"status" : 1
	},
	{
		"idx" : 1747,
		"title" : "조개도",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/y3bHrnsxOXmT",
		"status" : 1
	},
	{
		"idx" : 1748,
		"title" : "뚝도지기",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/italSUd1aTVn",
		"status" : 1
	},
	{
		"idx" : 1749,
		"title" : "오스테리아 파로",
		"score" : "4.4",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/U3sTmx0bWgn_",
		"status" : 1
	},
	{
		"idx" : 1750,
		"title" : "기연각",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/NJPBgqNmB4zo",
		"status" : 1
	},
	{
		"idx" : 1751,
		"title" : "옥수동 화덕피자",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/yryb7HvkPwFP",
		"status" : 1
	},
	{
		"idx" : 1752,
		"title" : "로우키",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/3LTRib0nn9cN",
		"status" : 1
	},
	{
		"idx" : 1753,
		"title" : "마테오견문록",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/7J-wRiChYddl",
		"status" : 1
	},
	{
		"idx" : 1754,
		"title" : "제스티살룬",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/-UUbd93wKH0H",
		"status" : 1
	},
	{
		"idx" : 1755,
		"title" : "미아논나",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/0h7MdjA_nhDS",
		"status" : 1
	},
	{
		"idx" : 1756,
		"title" : "제일곱창",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/zD8hOC0DZxT9",
		"status" : 1
	},
	{
		"idx" : 1757,
		"title" : "하노이102",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/v1o1-uKJee2c",
		"status" : 1
	},
	{
		"idx" : 1758,
		"title" : "빠오즈푸",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/NPbdF_Xc58N8",
		"status" : 1
	},
	{
		"idx" : 1759,
		"title" : "벱",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/cSzBVPbByHUX",
		"status" : 1
	},
	{
		"idx" : 1760,
		"title" : "패딩턴",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/MNThtYMWj1nD",
		"status" : 1
	},
	{
		"idx" : 1761,
		"title" : "원기옥",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/bDNhEqFJ2n-M",
		"status" : 1
	},
	{
		"idx" : 1762,
		"title" : "라프레플루트",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/qTuWq3GFeo8L",
		"status" : 1
	},
	{
		"idx" : 1763,
		"title" : "성수부두",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/6j2qZ3NDqmfD",
		"status" : 1
	},
	{
		"idx" : 1764,
		"title" : "코치",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/AGl0R3A9VaVE",
		"status" : 1
	},
	{
		"idx" : 1765,
		"title" : "목포산꽃게아구찜탕",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/44wa5wiIyY",
		"status" : 1
	},
	{
		"idx" : 1766,
		"title" : "잇샐러드",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/XI45Jwear2VA",
		"status" : 1
	},
	{
		"idx" : 1767,
		"title" : "먼치스앤구디스",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/jD9HM6Arc0Qm",
		"status" : 1
	},
	{
		"idx" : 1768,
		"title" : "청주한씨",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Gd-xWz0KKjit",
		"status" : 1
	},
	{
		"idx" : 1769,
		"title" : "인덕상점",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/HEwjdOeeG4wc",
		"status" : 1
	},
	{
		"idx" : 1770,
		"title" : "야마타니우동",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/gOknBRS_4rIv",
		"status" : 1
	},
	{
		"idx" : 1771,
		"title" : "바위파스타바",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/y3q7KXI2bjbM",
		"status" : 1
	},
	{
		"idx" : 1772,
		"title" : "들창코",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Ahdlx5FbSK",
		"status" : 1
	},
	{
		"idx" : 1773,
		"title" : "베티버",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/q4TaI9r3pMdg",
		"status" : 1
	},
	{
		"idx" : 1774,
		"title" : "위드번",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/IBHUy1awo6VY",
		"status" : 1
	},
	{
		"idx" : 1775,
		"title" : "정돈",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/GvmG6tH33BzB",
		"status" : 1
	},
	{
		"idx" : 1776,
		"title" : "마장황소곱창",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Hfk1vi5ZQa",
		"status" : 1
	},
	{
		"idx" : 1777,
		"title" : "성수온실",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/L2V0IbW4s0et",
		"status" : 1
	},
	{
		"idx" : 1778,
		"title" : "금호모소리",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/1WvWtCSoWNl4",
		"status" : 1
	},
	{
		"idx" : 1779,
		"title" : "밸런스포케",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/QTUUlivHdWaL",
		"status" : 1
	},
	{
		"idx" : 1780,
		"title" : "무쇠막생고기",
		"score" : "4.3",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/8aUdFgQXIpux",
		"status" : 1
	},
	{
		"idx" : 1781,
		"title" : "센터커피",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Nel5gICwJ98Y",
		"status" : 1
	},
	{
		"idx" : 1782,
		"title" : "어메이징브루잉컴퍼니",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/kfbJ9bNr-th7",
		"status" : 1
	},
	{
		"idx" : 1783,
		"title" : "우마텐텐동",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Ic_9hMizXHe2",
		"status" : 1
	},
	{
		"idx" : 1784,
		"title" : "로컬릿",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/f64TdDvo3XAo",
		"status" : 1
	},
	{
		"idx" : 1785,
		"title" : "맛차차",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/J5CwEKfiVHFq",
		"status" : 1
	},
	{
		"idx" : 1786,
		"title" : "매튜",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/mHuNqhztnkiN",
		"status" : 1
	},
	{
		"idx" : 1787,
		"title" : "아우프글렛",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/yzdZTWJfXXou",
		"status" : 1
	},
	{
		"idx" : 1788,
		"title" : "포지티브 서울숲",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/L-npHZFJXuDE",
		"status" : 1
	},
	{
		"idx" : 1789,
		"title" : "더코너키친",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/y2hb49e-tI",
		"status" : 1
	},
	{
		"idx" : 1790,
		"title" : "피키니키라자냐",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/iocZhc8DVI0m",
		"status" : 1
	},
	{
		"idx" : 1791,
		"title" : "쵸리상경",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/QLgOnVsjLYui",
		"status" : 1
	},
	{
		"idx" : 1792,
		"title" : "우동가조쿠",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/IcikbPUvaRHA",
		"status" : 1
	},
	{
		"idx" : 1793,
		"title" : "핏제리아 달 포르노",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/7zP0BzU_Q4VW",
		"status" : 1
	},
	{
		"idx" : 1794,
		"title" : "모찌모찌브래드",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/7CADLnhVnOao",
		"status" : 1
	},
	{
		"idx" : 1795,
		"title" : "단일서울",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/nFpKt5aCeZeV",
		"status" : 1
	},
	{
		"idx" : 1796,
		"title" : "만나떡볶이",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/NMBi75p8Aey1",
		"status" : 1
	},
	{
		"idx" : 1797,
		"title" : "일구공",
		"score" : "4.2",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/gnNX4XKYEoBH",
		"status" : 1
	},
	{
		"idx" : 1798,
		"title" : "윕 성수",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/hqx1Dfss4ODP",
		"status" : 1
	},
	{
		"idx" : 1799,
		"title" : "뚝도농원",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/_CQKwA2Jt1My",
		"status" : 1
	},
	{
		"idx" : 1800,
		"title" : "오부이용",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/eVPH47hTcaEv",
		"status" : 1
	},
	{
		"idx" : 1801,
		"title" : "타께리아 엘 몰리노",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Q_lVoY2ZLS97",
		"status" : 1
	},
	{
		"idx" : 1802,
		"title" : "꿉당",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Az2Ap4eT3Is_",
		"status" : 1
	},
	{
		"idx" : 1803,
		"title" : "위키드와이프",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Hr0iO3K08VZz",
		"status" : 1
	},
	{
		"idx" : 1804,
		"title" : "에이투비",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/b6zgdjXA5fI_",
		"status" : 1
	},
	{
		"idx" : 1805,
		"title" : "투그",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/uuSzEV-2XFT4",
		"status" : 1
	},
	{
		"idx" : 1806,
		"title" : "오스테리아 쟌니",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/EgCOfX1Ikfff",
		"status" : 1
	},
	{
		"idx" : 1807,
		"title" : "송계옥",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/TtNKRSQo-dNH",
		"status" : 1
	},
	{
		"idx" : 1808,
		"title" : "소바마에",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/kuyFO2CkHMeA",
		"status" : 1
	},
	{
		"idx" : 1809,
		"title" : "일품백송칼국수",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/mvg7W1hN7n",
		"status" : 1
	},
	{
		"idx" : 1810,
		"title" : "스탠드업플리즈바이턴온",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/ON4mgz4E3wi3",
		"status" : 1
	},
	{
		"idx" : 1811,
		"title" : "만두전빵",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/AujWK4CiHW",
		"status" : 1
	},
	{
		"idx" : 1812,
		"title" : "진국설렁탕",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/muarMKlVyF",
		"status" : 1
	},
	{
		"idx" : 1813,
		"title" : "에피타이트",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/WMxG6NIST64G",
		"status" : 1
	},
	{
		"idx" : 1814,
		"title" : "이월로스터스",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/RJ4jR4efjXUt",
		"status" : 1
	},
	{
		"idx" : 1815,
		"title" : "메종파이프그라운드",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/TzGD7Noce3tD",
		"status" : 1
	},
	{
		"idx" : 1816,
		"title" : "티룸",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/ffKe2k6q_HKK",
		"status" : 1
	},
	{
		"idx" : 1817,
		"title" : "몽실이네토종한우",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/PVyrnW_Hbo",
		"status" : 1
	},
	{
		"idx" : 1818,
		"title" : "햄서울",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/dT3VpcMJIGUI",
		"status" : 1
	},
	{
		"idx" : 1819,
		"title" : "오레노카츠",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Q2NHEIunbfdF",
		"status" : 1
	},
	{
		"idx" : 1820,
		"title" : "백정돈공장",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/8Q6s0jjF47tr",
		"status" : 1
	},
	{
		"idx" : 1821,
		"title" : "스트로베리32",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Vq3_Wnq2hEpB",
		"status" : 1
	},
	{
		"idx" : 1822,
		"title" : "몽쥬빠티세리",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/0aBagkE50AXo",
		"status" : 1
	},
	{
		"idx" : 1823,
		"title" : "다포케",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/k532mgQjqEnX",
		"status" : 1
	},
	{
		"idx" : 1824,
		"title" : "카페노티드",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/-hVY6FbK65Rr",
		"status" : 1
	},
	{
		"idx" : 1825,
		"title" : "아트몬스터",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/8pv5HyAMkcly",
		"status" : 1
	},
	{
		"idx" : 1826,
		"title" : "로우커피스탠드",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/_wSiV5ECWkAW",
		"status" : 1
	},
	{
		"idx" : 1827,
		"title" : "니드스윗",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/48rvBvszbgJ0",
		"status" : 1
	},
	{
		"idx" : 1828,
		"title" : "소인수서울",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/54bJ2HHcl8tW",
		"status" : 1
	},
	{
		"idx" : 1829,
		"title" : "크림라벨",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/3LQS7_L0NCXk",
		"status" : 1
	},
	{
		"idx" : 1830,
		"title" : "어니언",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/duy5i8oeIhBy",
		"status" : 1
	},
	{
		"idx" : 1831,
		"title" : "소문난성수감자탕",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/EkyrAzkXyC",
		"status" : 1
	},
	{
		"idx" : 1832,
		"title" : "멜로워커피",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/_Zra2SvxcNMH",
		"status" : 1
	},
	{
		"idx" : 1833,
		"title" : "바이 레인",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/K6Z8LbaADyQT",
		"status" : 1
	},
	{
		"idx" : 1834,
		"title" : "커피식탁",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/_ewboym4wZbW",
		"status" : 1
	},
	{
		"idx" : 1835,
		"title" : "오므오트",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/wSpv3JFWuZQ5",
		"status" : 1
	},
	{
		"idx" : 1836,
		"title" : "엑셀플레이스",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/zAmXlMEK8r36",
		"status" : 1
	},
	{
		"idx" : 1837,
		"title" : "청죽골식당",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/OqhzuMztXw",
		"status" : 1
	},
	{
		"idx" : 1838,
		"title" : "한양대신닭발",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/tvc-HavF2GYt",
		"status" : 1
	},
	{
		"idx" : 1839,
		"title" : "다운타우너",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/bmpQx6yvbHYt",
		"status" : 1
	},
	{
		"idx" : 1840,
		"title" : "옥수해물찜칼국수",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/k9VttNz9Pg",
		"status" : 1
	},
	{
		"idx" : 1841,
		"title" : "고공",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/B18kI-Yx8Gaa",
		"status" : 1
	},
	{
		"idx" : 1842,
		"title" : "코끼리베이글",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/cVoHdz0WwOhm",
		"status" : 1
	},
	{
		"idx" : 1843,
		"title" : "까사다루아",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/yqbg5fZ1sxei",
		"status" : 1
	},
	{
		"idx" : 1844,
		"title" : "샐피",
		"score" : "4.1",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/dr86opcd19dK",
		"status" : 1
	},
	{
		"idx" : 1845,
		"title" : "밀도",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/-YaZZzN1JW",
		"status" : 1
	},
	{
		"idx" : 1846,
		"title" : "푸줏간생고기점",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/g6pOoH8Aid",
		"status" : 1
	},
	{
		"idx" : 1847,
		"title" : "마구로쇼쿠도",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/uxjkniX9gR7V",
		"status" : 1
	},
	{
		"idx" : 1848,
		"title" : "앤드밀",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/JFDusvTg6ZUD",
		"status" : 1
	},
	{
		"idx" : 1849,
		"title" : "꾸아",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/ZqncAc58gBnx",
		"status" : 1
	},
	{
		"idx" : 1850,
		"title" : "뺑드에코",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/ABnwC-br7013",
		"status" : 1
	},
	{
		"idx" : 1851,
		"title" : "봉순이네다락방",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/91bf3_JkIE",
		"status" : 1
	},
	{
		"idx" : 1852,
		"title" : "쓰리오브어스",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/-tQtweHUn1MB",
		"status" : 1
	},
	{
		"idx" : 1853,
		"title" : "온더",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/eLqWTA8ndVj9",
		"status" : 1
	},
	{
		"idx" : 1854,
		"title" : "푼토돌체 (휴업중)",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/zxb0hZ8CqhSF",
		"status" : 1
	},
	{
		"idx" : 1855,
		"title" : "애리꼼닭발",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/b4fe0mCqQp",
		"status" : 1
	},
	{
		"idx" : 1856,
		"title" : "마케나이데",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/t3UkVi6MwF6J",
		"status" : 1
	},
	{
		"idx" : 1857,
		"title" : "일품생고기",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/ixJvU_hme5",
		"status" : 1
	},
	{
		"idx" : 1858,
		"title" : "미도림",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Ha-RjMRFLWAZ",
		"status" : 1
	},
	{
		"idx" : 1859,
		"title" : "프라이데이무브먼트",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/H4PK2xN09q_v",
		"status" : 1
	},
	{
		"idx" : 1860,
		"title" : "키커피 컴퍼니",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/GlsuhebHEyfT",
		"status" : 1
	},
	{
		"idx" : 1861,
		"title" : "굴림",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/njzgx3jDanvp",
		"status" : 1
	},
	{
		"idx" : 1862,
		"title" : "파티세리후르츠",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/oqD3q6BS4HdS",
		"status" : 1
	},
	{
		"idx" : 1863,
		"title" : "에르제",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Z6Xs0L2MQvWO",
		"status" : 1
	},
	{
		"idx" : 1864,
		"title" : "모멘토브루어스",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/GHTApDBASSrw",
		"status" : 1
	},
	{
		"idx" : 1865,
		"title" : "메쉬커피",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/7eysRhOffWqs",
		"status" : 1
	},
	{
		"idx" : 1866,
		"title" : "훼미리손칼국수",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/v5Wg3lT1rHDI",
		"status" : 1
	},
	{
		"idx" : 1867,
		"title" : "청키드",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/qiCh8fwIx_Xn",
		"status" : 1
	},
	{
		"idx" : 1868,
		"title" : "파티세리아모니",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/x0yFu_layUHw",
		"status" : 1
	},
	{
		"idx" : 1869,
		"title" : "칙피스",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/VS85yREGut2C",
		"status" : 1
	},
	{
		"idx" : 1870,
		"title" : "퍼주에",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/zi5BwSHIcQ3z",
		"status" : 1
	},
	{
		"idx" : 1871,
		"title" : "도믹스",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/R6uD2QzF9gjc",
		"status" : 1
	},
	{
		"idx" : 1872,
		"title" : "미디엄스톤",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/t6l2rSnQmkRw",
		"status" : 1
	},
	{
		"idx" : 1873,
		"title" : "멘야코노하",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/VdUHmXbDH1HF",
		"status" : 1
	},
	{
		"idx" : 1874,
		"title" : "연텐동",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/F8vfPLYM9_DR",
		"status" : 1
	},
	{
		"idx" : 1875,
		"title" : "스테치",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/PcOwFIC0OcDj",
		"status" : 1
	},
	{
		"idx" : 1876,
		"title" : "진작다이닝",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/Q3iAuj0vneFE",
		"status" : 1
	},
	{
		"idx" : 1877,
		"title" : "기미사",
		"score" : "3.9",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/wx07WbQV15kP",
		"status" : 1
	},
	{
		"idx" : 1878,
		"title" : "옹근달",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/4WINNgmLzX6_",
		"status" : 1
	},
	{
		"idx" : 1879,
		"title" : "문츠바베큐",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/PhVoleNRQf0O",
		"status" : 1
	},
	{
		"idx" : 1880,
		"title" : "부부요리단1탄 제주흑돼지갑오징어",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/SOBbQ4oSwl",
		"status" : 1
	},
	{
		"idx" : 1881,
		"title" : "갈십리",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/XemAGxqP12n_",
		"status" : 1
	},
	{
		"idx" : 1882,
		"title" : "롸카두들내쉬빌핫치킨",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/M54tSI-6cvGW",
		"status" : 1
	},
	{
		"idx" : 1883,
		"title" : "꼬랑치킨",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/ImrDlLuEU4zk",
		"status" : 1
	},
	{
		"idx" : 1884,
		"title" : "더파머스카페",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/oo1w3XiR_-di",
		"status" : 1
	},
	{
		"idx" : 1885,
		"title" : "더즌오이스터",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/zZ33B1-hoIqh",
		"status" : 1
	},
	{
		"idx" : 1886,
		"title" : "까까를로",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/he4ma_s3PJxy",
		"status" : 1
	},
	{
		"idx" : 1887,
		"title" : "페이퍼플레이트",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/dRfG67kGG7iH",
		"status" : 1
	},
	{
		"idx" : 1888,
		"title" : "낙원스낵",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/78zM7M3_uzIu",
		"status" : 1
	},
	{
		"idx" : 1889,
		"title" : "테이퍼드커피",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/aRmDGEJIv9Xp",
		"status" : 1
	},
	{
		"idx" : 1890,
		"title" : "5to7",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/1CqCo1j8J-KC",
		"status" : 1
	},
	{
		"idx" : 1891,
		"title" : "왕십리정부네곱창",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/ct9OV91v7j",
		"status" : 1
	},
	{
		"idx" : 1892,
		"title" : "버섯집",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/RDnApBSj6BZd",
		"status" : 1
	},
	{
		"idx" : 1893,
		"title" : "잠수교집",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/ygxC0_dfxAjQ",
		"status" : 1
	},
	{
		"idx" : 1894,
		"title" : "동방양꼬치",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/oh5viHoUTK",
		"status" : 1
	},
	{
		"idx" : 1895,
		"title" : "토상막회",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/dlhMVhmQWm",
		"status" : 1
	},
	{
		"idx" : 1896,
		"title" : "유가츠",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/bDlA_Y0d3GCK",
		"status" : 1
	},
	{
		"idx" : 1897,
		"title" : "유스트레스",
		"score" : "4.0",
		"region" : "성동구",
		"url" : "https://www.mangoplate.com/restaurants/IibfkFans7Nf",
		"status" : 1
	},
	{
		"idx" : 1898,
		"title" : "가츠시",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/J2YQUa--FYYW",
		"status" : 1
	},
	{
		"idx" : 1899,
		"title" : "쭈꾸미킹",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/uvaBKkr42J",
		"status" : 1
	},
	{
		"idx" : 1900,
		"title" : "투또톤토 에스프레소바",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/loADxCRlNPEa",
		"status" : 1
	},
	{
		"idx" : 1901,
		"title" : "띵똥와플",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/pPBMOqT36q",
		"status" : 1
	},
	{
		"idx" : 1902,
		"title" : "호파스타",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/EOKWSBbbrDOy",
		"status" : 1
	},
	{
		"idx" : 1903,
		"title" : "벨롱에스프레소",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/qTmAYLRlPZy5",
		"status" : 1
	},
	{
		"idx" : 1904,
		"title" : "요마시",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/HSeRi1xSMStd",
		"status" : 1
	},
	{
		"idx" : 1905,
		"title" : "모츠커피",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/x-3Rixs8YBQu",
		"status" : 1
	},
	{
		"idx" : 1906,
		"title" : "천향마라탕",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/ppseGr-250su",
		"status" : 1
	},
	{
		"idx" : 1907,
		"title" : "메종드타르트",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/VAKL0rg3AJ",
		"status" : 1
	},
	{
		"idx" : 1908,
		"title" : "애드앤드",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/4Ni1ou4TQMBy",
		"status" : 1
	},
	{
		"idx" : 1909,
		"title" : "화원",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/xmje2mmgub",
		"status" : 1
	},
	{
		"idx" : 1910,
		"title" : "옥루몽",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/EbShRUHWEH",
		"status" : 1
	},
	{
		"idx" : 1911,
		"title" : "대원칼국수",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/j14eSszZb-",
		"status" : 1
	},
	{
		"idx" : 1912,
		"title" : "부리또피아",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/qZksmM7LHGQH",
		"status" : 1
	},
	{
		"idx" : 1913,
		"title" : "포크포크",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/W-fYeCn88jb5",
		"status" : 1
	},
	{
		"idx" : 1914,
		"title" : "호야초밥참치전문점",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/NFuvdGzFAV",
		"status" : 1
	},
	{
		"idx" : 1915,
		"title" : "감성당",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/-_mouGL7-ZY4",
		"status" : 1
	},
	{
		"idx" : 1916,
		"title" : "쿵푸소룽샤",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/LokP8bMapfaE",
		"status" : 1
	},
	{
		"idx" : 1917,
		"title" : "다원식당",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/BkMHw8kU_dtb",
		"status" : 1
	},
	{
		"idx" : 1918,
		"title" : "주하객잔",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/xMdZ7LSt5-or",
		"status" : 1
	},
	{
		"idx" : 1919,
		"title" : "순금이떡볶이",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Bq03T0tppa",
		"status" : 1
	},
	{
		"idx" : 1920,
		"title" : "심야식당 쿠난",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/M-ulNMc2dgh6",
		"status" : 1
	},
	{
		"idx" : 1921,
		"title" : "소사면옥",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Xw7nDKYXeD3l",
		"status" : 1
	},
	{
		"idx" : 1922,
		"title" : "Daughter",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/MMcsUBVqgawD",
		"status" : 1
	},
	{
		"idx" : 1923,
		"title" : "스시오리",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/NQZXlc7MvB_c",
		"status" : 1
	},
	{
		"idx" : 1924,
		"title" : "또래끼리",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Tm8e4Crbh0eE",
		"status" : 1
	},
	{
		"idx" : 1925,
		"title" : "훈춘양꼬치",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/OsFezN2UCdM_",
		"status" : 1
	},
	{
		"idx" : 1926,
		"title" : "함루",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/-t3Ra-Ka-wyL",
		"status" : 1
	},
	{
		"idx" : 1927,
		"title" : "신토불이떡볶이",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/NH7ubGRQvg",
		"status" : 1
	},
	{
		"idx" : 1928,
		"title" : "꼬메노",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/qAPlBXD0vD",
		"status" : 1
	},
	{
		"idx" : 1929,
		"title" : "사월식당",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/WX16nZzHAdgU",
		"status" : 1
	},
	{
		"idx" : 1930,
		"title" : "모서리에커피집",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/RdtLTVtW7v",
		"status" : 1
	},
	{
		"idx" : 1931,
		"title" : "계탄집",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/aWU6nheW3YK6",
		"status" : 1
	},
	{
		"idx" : 1932,
		"title" : "로얄인디안레스토랑",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/t4gD6A2Viv",
		"status" : 1
	},
	{
		"idx" : 1933,
		"title" : "칼레오커피로스터스",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Zpa1eGGk6b",
		"status" : 1
	},
	{
		"idx" : 1934,
		"title" : "건대커피랩",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/RZIN40rCp8",
		"status" : 1
	},
	{
		"idx" : 1935,
		"title" : "하이디라오",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/L4_cu-BNSdEi",
		"status" : 1
	},
	{
		"idx" : 1936,
		"title" : "고래바",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/2p4Y5WNrutqb",
		"status" : 1
	},
	{
		"idx" : 1937,
		"title" : "산골닭갈비",
		"score" : "3.9",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/VGYgGFs99X",
		"status" : 1
	},
	{
		"idx" : 1938,
		"title" : "케루악",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/VH0ecz1WPnMg",
		"status" : 1
	},
	{
		"idx" : 1939,
		"title" : "포비",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/P2MIDqJm1R9k",
		"status" : 1
	},
	{
		"idx" : 1940,
		"title" : "로이베이커리카페",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/nSjfvuBLxTlj",
		"status" : 1
	},
	{
		"idx" : 1941,
		"title" : "반티엔야오 카오위",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/sC1etteyiLHR",
		"status" : 1
	},
	{
		"idx" : 1942,
		"title" : "알고",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/wiicCqLHcgzg",
		"status" : 1
	},
	{
		"idx" : 1943,
		"title" : "환이네갈비살",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/BzQzcyC7aNiS",
		"status" : 1
	},
	{
		"idx" : 1944,
		"title" : "횃불",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/fDKjNqm88UR1",
		"status" : 1
	},
	{
		"idx" : 1945,
		"title" : "강쇠네",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/0JZklw1Wxr",
		"status" : 1
	},
	{
		"idx" : 1946,
		"title" : "선장훅",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/WI3bgsULlJvs",
		"status" : 1
	},
	{
		"idx" : 1947,
		"title" : "서북면옥",
		"score" : "4.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/nIAL5CoZOW",
		"status" : 1
	},
	{
		"idx" : 1948,
		"title" : "경성양육관",
		"score" : "4.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/fR7_wxANKzKN",
		"status" : 1
	},
	{
		"idx" : 1949,
		"title" : "콩이네",
		"score" : "4.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/mhsM8sgsmKtx",
		"status" : 1
	},
	{
		"idx" : 1950,
		"title" : "비에이치테이블",
		"score" : "4.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/p1fCHp49ucfA",
		"status" : 1
	},
	{
		"idx" : 1951,
		"title" : "나루떡볶이",
		"score" : "4.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/drWLLlchhgwD",
		"status" : 1
	},
	{
		"idx" : 1952,
		"title" : "드로잉레시피",
		"score" : "4.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/xfsl3Vy8bsyW",
		"status" : 1
	},
	{
		"idx" : 1953,
		"title" : "스위트앤카츠",
		"score" : "4.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/v2T6cXqOtLyQ",
		"status" : 1
	},
	{
		"idx" : 1954,
		"title" : "얼땅쟈",
		"score" : "4.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/nj3Hk9TB47dT",
		"status" : 1
	},
	{
		"idx" : 1955,
		"title" : "준성이네",
		"score" : "4.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/zrCsa9TewVyO",
		"status" : 1
	},
	{
		"idx" : 1956,
		"title" : "피자힐",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/U1Y1QuTMox",
		"status" : 1
	},
	{
		"idx" : 1957,
		"title" : "우마이도",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/-8CFTwiB41",
		"status" : 1
	},
	{
		"idx" : 1958,
		"title" : "텐동한",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/lz14nvWzcTqx",
		"status" : 1
	},
	{
		"idx" : 1959,
		"title" : "라멘다이야",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/kJdVxYa5HLm3",
		"status" : 1
	},
	{
		"idx" : 1960,
		"title" : "송화산시도삭면",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/K2TXHsay6ieT",
		"status" : 1
	},
	{
		"idx" : 1961,
		"title" : "영미오리탕",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/ZlVnEI7B2r",
		"status" : 1
	},
	{
		"idx" : 1962,
		"title" : "미식반점",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/JL_NnZ56pi5a",
		"status" : 1
	},
	{
		"idx" : 1963,
		"title" : "일레븐 라운지",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/nv2bKK6yWvfU",
		"status" : 1
	},
	{
		"idx" : 1964,
		"title" : "이씨주방",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/5ouH9H06eH",
		"status" : 1
	},
	{
		"idx" : 1965,
		"title" : "샤오롱바오",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/JL6nQfyBRGRS",
		"status" : 1
	},
	{
		"idx" : 1966,
		"title" : "최가커피회관",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/qD-H4KmoLN4m",
		"status" : 1
	},
	{
		"idx" : 1967,
		"title" : "르파사쥬",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/5lod-1QWnE8T",
		"status" : 1
	},
	{
		"idx" : 1968,
		"title" : "밍지황먼지찜닭",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/kwGiLhyL4MSk",
		"status" : 1
	},
	{
		"idx" : 1969,
		"title" : "더이퀼리브리엄커피",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/M9VIeRbkKyh2",
		"status" : 1
	},
	{
		"idx" : 1970,
		"title" : "민정식당",
		"score" : "4.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/RLl1E4nXWI",
		"status" : 1
	},
	{
		"idx" : 1971,
		"title" : "소바쿠",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/3dXE__KRWcOv",
		"status" : 1
	},
	{
		"idx" : 1972,
		"title" : "해룡마라룽샤",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/m_pXgUzp4Plg",
		"status" : 1
	},
	{
		"idx" : 1973,
		"title" : "Index",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Rhsje7e-UuxC",
		"status" : 1
	},
	{
		"idx" : 1974,
		"title" : "태천면옥",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/JUsGTjz2Kq_R",
		"status" : 1
	},
	{
		"idx" : 1975,
		"title" : "마우로아",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/UaOsgipzYOHy",
		"status" : 1
	},
	{
		"idx" : 1976,
		"title" : "화양식당",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/H5-9R9umUyJO",
		"status" : 1
	},
	{
		"idx" : 1977,
		"title" : "수퍼슬라이더스",
		"score" : "4.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/oJPy2iHM3clM",
		"status" : 1
	},
	{
		"idx" : 1978,
		"title" : "오코노미야키식당하나",
		"score" : "4.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/RTC_u7jrxHMl",
		"status" : 1
	},
	{
		"idx" : 1979,
		"title" : "플록",
		"score" : "4.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/BBKgCvGOrJ-K",
		"status" : 1
	},
	{
		"idx" : 1980,
		"title" : "시홍쓰",
		"score" : "4.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/L6LQdsD4NSLy",
		"status" : 1
	},
	{
		"idx" : 1981,
		"title" : "송화산시도삭면",
		"score" : "4.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/f2yM7Ac3f--8",
		"status" : 1
	},
	{
		"idx" : 1982,
		"title" : "뚝방길 홍차가게",
		"score" : "4.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/JH3bhstVpYnz",
		"status" : 1
	},
	{
		"idx" : 1983,
		"title" : "명봉반점",
		"score" : "4.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/-G-YWwpe9D",
		"status" : 1
	},
	{
		"idx" : 1984,
		"title" : "원조할아버지손두부",
		"score" : "4.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/GOcaPhTY0fTg",
		"status" : 1
	},
	{
		"idx" : 1985,
		"title" : "매운향솥",
		"score" : "4.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Co_h796vv0",
		"status" : 1
	},
	{
		"idx" : 1986,
		"title" : "멕시칼리",
		"score" : "4.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/kVU1bi4E1OMj",
		"status" : 1
	},
	{
		"idx" : 1987,
		"title" : "피읖",
		"score" : "4.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/e7yrBrzeA0wQ",
		"status" : 1
	},
	{
		"idx" : 1988,
		"title" : "남한강민물매운탕",
		"score" : "4.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/GWQyZs33yd0j",
		"status" : 1
	},
	{
		"idx" : 1989,
		"title" : "초라멘",
		"score" : "4.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Qnbd3LP8Dds1",
		"status" : 1
	},
	{
		"idx" : 1990,
		"title" : "이화만두",
		"score" : "4.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/njfFtxm7B-PE",
		"status" : 1
	},
	{
		"idx" : 1991,
		"title" : "빠오즈푸",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/OaKrC5BEc1",
		"status" : 1
	},
	{
		"idx" : 1992,
		"title" : "이이요",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/lmV7-IPVgD3m",
		"status" : 1
	},
	{
		"idx" : 1993,
		"title" : "대흥양다리바베큐",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/ZgqmI6Gc8H",
		"status" : 1
	},
	{
		"idx" : 1994,
		"title" : "육성회비",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/1-l0js5-m1",
		"status" : 1
	},
	{
		"idx" : 1995,
		"title" : "송화양꼬치",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/NbzLooP_jM",
		"status" : 1
	},
	{
		"idx" : 1996,
		"title" : "라라관",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/8h4RYSgAjvJU",
		"status" : 1
	},
	{
		"idx" : 1997,
		"title" : "김돈이",
		"score" : "4.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/LsqwEAlDvs",
		"status" : 1
	},
	{
		"idx" : 1998,
		"title" : "카페 아르무아",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/ckAYZjwHIhA8",
		"status" : 1
	},
	{
		"idx" : 1999,
		"title" : "체리커피",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/o9_eN6FsNhci",
		"status" : 1
	},
	{
		"idx" : 2000,
		"title" : "명월관",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/HC7_phKpJe",
		"status" : 1
	},
	{
		"idx" : 2001,
		"title" : "건대스시",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/HdCTUmA8bX",
		"status" : 1
	},
	{
		"idx" : 2002,
		"title" : "심마니",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/5v5DH7MtlR",
		"status" : 1
	},
	{
		"idx" : 2003,
		"title" : "겐로쿠우동",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/OfNy1w3NF9",
		"status" : 1
	},
	{
		"idx" : 2004,
		"title" : "아오스요거트",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/cf6dmPNM2cYM",
		"status" : 1
	},
	{
		"idx" : 2005,
		"title" : "메호르",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/DpylTzH-C-1Y",
		"status" : 1
	},
	{
		"idx" : 2006,
		"title" : "골목료리집",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/CrjzP7ZxR4jS",
		"status" : 1
	},
	{
		"idx" : 2007,
		"title" : "카페드라이",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/IPJq1RPuz9AJ",
		"status" : 1
	},
	{
		"idx" : 2008,
		"title" : "민벅",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/9RSryP1I75",
		"status" : 1
	},
	{
		"idx" : 2009,
		"title" : "보난자커피",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Qpzqf9pBDgMH",
		"status" : 1
	},
	{
		"idx" : 2010,
		"title" : "메이빌",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/AuVUqhfIY0",
		"status" : 1
	},
	{
		"idx" : 2011,
		"title" : "아날로그키친",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Dg8sSZRfl-",
		"status" : 1
	},
	{
		"idx" : 2012,
		"title" : "Cafe k375",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/RzPUDa7tDzkV",
		"status" : 1
	},
	{
		"idx" : 2013,
		"title" : "은혜떡볶이",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/zDbFPBYsF9",
		"status" : 1
	},
	{
		"idx" : 2014,
		"title" : "LAB41",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Q7nDIlK_oFA1",
		"status" : 1
	},
	{
		"idx" : 2015,
		"title" : "뺑드램",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/gGxjuCo3to",
		"status" : 1
	},
	{
		"idx" : 2016,
		"title" : "실란트로커피",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/gx7B1aJgaX1I",
		"status" : 1
	},
	{
		"idx" : 2017,
		"title" : "돕감자탕전문점",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/TamtXYgkqA",
		"status" : 1
	},
	{
		"idx" : 2018,
		"title" : "뱃놈",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/gR0_1lEOfdtf",
		"status" : 1
	},
	{
		"idx" : 2019,
		"title" : "스시텐",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/VSYekXqSJP",
		"status" : 1
	},
	{
		"idx" : 2020,
		"title" : "왕십리정곱창",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Nx2V0BakAd",
		"status" : 1
	},
	{
		"idx" : 2021,
		"title" : "보라젤라또",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Aw0yolPZKJPF",
		"status" : 1
	},
	{
		"idx" : 2022,
		"title" : "사대분식",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/tXHEZm_4_D",
		"status" : 1
	},
	{
		"idx" : 2023,
		"title" : "엘루이피자앤펍",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/4Py4xNcLdfjO",
		"status" : 1
	},
	{
		"idx" : 2024,
		"title" : "건대우동집",
		"score" : "3.8",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Qa4NBKp5S3h4",
		"status" : 1
	},
	{
		"idx" : 2025,
		"title" : "봉자마라탕",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/U__YsyMXsBuB",
		"status" : 1
	},
	{
		"idx" : 2026,
		"title" : "미분당",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/9AiCKGUx3SV0",
		"status" : 1
	},
	{
		"idx" : 2027,
		"title" : "더뷔페",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/FyZ6C3c9ZD",
		"status" : 1
	},
	{
		"idx" : 2028,
		"title" : "이우",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/7Z6ueLRBh6Pr",
		"status" : 1
	},
	{
		"idx" : 2029,
		"title" : "복만루",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/dLa6suRZKy",
		"status" : 1
	},
	{
		"idx" : 2030,
		"title" : "해피니스디저트",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/zNAj0ACp9K9U",
		"status" : 1
	},
	{
		"idx" : 2031,
		"title" : "청와옥",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Lqp4pmqIJebj",
		"status" : 1
	},
	{
		"idx" : 2032,
		"title" : "단골손님",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/9g0UCF3S5YYh",
		"status" : 1
	},
	{
		"idx" : 2033,
		"title" : "강릉엄지네꼬막집",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/pi_C0bwP2r9h",
		"status" : 1
	},
	{
		"idx" : 2034,
		"title" : "옛집",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/x3VEryZ6An",
		"status" : 1
	},
	{
		"idx" : 2035,
		"title" : "사보텐",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/YKO_f4qTjFXg",
		"status" : 1
	},
	{
		"idx" : 2036,
		"title" : "고흥순대국머리고기",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Zrui0KLVNC",
		"status" : 1
	},
	{
		"idx" : 2037,
		"title" : "니뽕내뽕",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/O6jCxDHItH",
		"status" : 1
	},
	{
		"idx" : 2038,
		"title" : "광어2마리",
		"score" : "3.4",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/WIrZbQCleK",
		"status" : 1
	},
	{
		"idx" : 2039,
		"title" : "홍대돈부리",
		"score" : "3.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/NqzcnTZnvj",
		"status" : 1
	},
	{
		"idx" : 2040,
		"title" : "송림식당",
		"score" : "3.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/KBIk_TgpJE",
		"status" : 1
	},
	{
		"idx" : 2041,
		"title" : "마우스래빗",
		"score" : "3.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/Fr4rxSx0MK",
		"status" : 1
	},
	{
		"idx" : 2042,
		"title" : "페스타마레",
		"score" : "3.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/DN9EOy9yVd",
		"status" : 1
	},
	{
		"idx" : 2043,
		"title" : "잉글사이드",
		"score" : "3.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/00W4j8LkKxwn",
		"status" : 1
	},
	{
		"idx" : 2044,
		"title" : "화기애애",
		"score" : "3.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/FD56FNRkdC",
		"status" : 1
	},
	{
		"idx" : 2045,
		"title" : "커피마켓",
		"score" : "3.3",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/-KYjmbQrAX",
		"status" : 1
	},
	{
		"idx" : 2046,
		"title" : "신사소곱창",
		"score" : "3.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/S9vJwnEp3m",
		"status" : 1
	},
	{
		"idx" : 2047,
		"title" : "설빙",
		"score" : "3.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/tWgttlKk6X",
		"status" : 1
	},
	{
		"idx" : 2048,
		"title" : "도치피자",
		"score" : "3.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/XSD8_0nhj8Yq",
		"status" : 1
	},
	{
		"idx" : 2049,
		"title" : "모모스테이크",
		"score" : "3.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/6r_6yEarub",
		"status" : 1
	},
	{
		"idx" : 2050,
		"title" : "봉추찜닭",
		"score" : "3.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/I8JPBDC3M1",
		"status" : 1
	},
	{
		"idx" : 2051,
		"title" : "육회한연어",
		"score" : "3.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/df5Lj1OGwVAP",
		"status" : 1
	},
	{
		"idx" : 2052,
		"title" : "메차쿠차",
		"score" : "3.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/vgpMAqv9m1",
		"status" : 1
	},
	{
		"idx" : 2053,
		"title" : "본가칼국수",
		"score" : "3.2",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/xIoNWly5hkni",
		"status" : 1
	},
	{
		"idx" : 2054,
		"title" : "금룡",
		"score" : "3.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/dpmUjved2-",
		"status" : 1
	},
	{
		"idx" : 2055,
		"title" : "범가",
		"score" : "3.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/mq0PCNg2k0",
		"status" : 1
	},
	{
		"idx" : 2056,
		"title" : "바나나토크",
		"score" : "3.1",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/fFeP-5-hSs",
		"status" : 1
	},
	{
		"idx" : 2057,
		"title" : "라화쿵부",
		"score" : "3.0",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/xc3kFB_Pgf",
		"status" : 1
	},
	{
		"idx" : 2058,
		"title" : "중경소면관",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/207PnvGFNqFG",
		"status" : 1
	},
	{
		"idx" : 2059,
		"title" : "하루",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/VSYcX9N4LhsA",
		"status" : 1
	},
	{
		"idx" : 2060,
		"title" : "노다메",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/XADtA63zaY",
		"status" : 1
	},
	{
		"idx" : 2061,
		"title" : "라구뜨",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/O1HMZeIsir",
		"status" : 1
	},
	{
		"idx" : 2062,
		"title" : "래빗홀 버거컴퍼니",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/aEJqzlRkzxkY",
		"status" : 1
	},
	{
		"idx" : 2063,
		"title" : "반둥식당",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/YxXSydClb08q",
		"status" : 1
	},
	{
		"idx" : 2064,
		"title" : "아찌떡볶이",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/gQR3Sh7P-0",
		"status" : 1
	},
	{
		"idx" : 2065,
		"title" : "초밥짓는원숭이",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/tKZ8U5d3Gg",
		"status" : 1
	},
	{
		"idx" : 2066,
		"title" : "콩불",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/hY5IH6tTM3",
		"status" : 1
	},
	{
		"idx" : 2067,
		"title" : "능동샐러드",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/w6jFMVR-2XBR",
		"status" : 1
	},
	{
		"idx" : 2068,
		"title" : "그자체베이커리카페",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/e02mPcMrnHJY",
		"status" : 1
	},
	{
		"idx" : 2069,
		"title" : "능동국시",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/hV6X3i0Nd8ST",
		"status" : 1
	},
	{
		"idx" : 2070,
		"title" : "열매제과점",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/E_sacq_fLAj0",
		"status" : 1
	},
	{
		"idx" : 2071,
		"title" : "더파빌리온",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/w3eck49pj7",
		"status" : 1
	},
	{
		"idx" : 2072,
		"title" : "조씨네고기국수",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/HHOGgltRGsn9",
		"status" : 1
	},
	{
		"idx" : 2073,
		"title" : "함흥본가면옥",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/bmltc2s9Ld",
		"status" : 1
	},
	{
		"idx" : 2074,
		"title" : "어반나이프",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/3f_cygfY_M",
		"status" : 1
	},
	{
		"idx" : 2075,
		"title" : "도쿄빙수",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/jjfn4pnA0Pfw",
		"status" : 1
	},
	{
		"idx" : 2076,
		"title" : "복만루",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/guas4p3WYTe_",
		"status" : 1
	},
	{
		"idx" : 2077,
		"title" : "아차산손두부",
		"score" : "3.5",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/rWDQGA1Ven",
		"status" : 1
	},
	{
		"idx" : 2078,
		"title" : "궤도에오르다",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/ezYqeGHlXFi1",
		"status" : 1
	},
	{
		"idx" : 2079,
		"title" : "장순루",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/ajfWFzhMMD",
		"status" : 1
	},
	{
		"idx" : 2080,
		"title" : "미주류",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/ySvb7DtWR643",
		"status" : 1
	},
	{
		"idx" : 2081,
		"title" : "고향양꼬치",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/dg54uW6D2U",
		"status" : 1
	},
	{
		"idx" : 2082,
		"title" : "최신족발",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/RPxTaZHuDA",
		"status" : 1
	},
	{
		"idx" : 2083,
		"title" : "깍뚝",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/-bj-J2GYQse6",
		"status" : 1
	},
	{
		"idx" : 2084,
		"title" : "부탄츄",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/yOiXqn_0sKRD",
		"status" : 1
	},
	{
		"idx" : 2085,
		"title" : "유키노하나",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/EzNNA2jOUyMl",
		"status" : 1
	},
	{
		"idx" : 2086,
		"title" : "멘쇼",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/MB2btizNRglV",
		"status" : 1
	},
	{
		"idx" : 2087,
		"title" : "매화반점",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/L26FTOyuzn",
		"status" : 1
	},
	{
		"idx" : 2088,
		"title" : "정면",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/JqxWsjV91Z5t",
		"status" : 1
	},
	{
		"idx" : 2089,
		"title" : "프언타이",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/1BBuC73-mKic",
		"status" : 1
	},
	{
		"idx" : 2090,
		"title" : "카페래디언트",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/p9fri4yaXcNN",
		"status" : 1
	},
	{
		"idx" : 2091,
		"title" : "민속손국시",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/swWF9sB6ac",
		"status" : 1
	},
	{
		"idx" : 2092,
		"title" : "청두인상",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/wi6Mn-RXBx4y",
		"status" : 1
	},
	{
		"idx" : 2093,
		"title" : "포비의 행방불명",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/vK_NrW1VcuhP",
		"status" : 1
	},
	{
		"idx" : 2094,
		"title" : "아웃닭",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/1v8q1Tbb-NAa",
		"status" : 1
	},
	{
		"idx" : 2095,
		"title" : "솔티드",
		"score" : "3.7",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/djaK53zRkQ5h",
		"status" : 1
	},
	{
		"idx" : 2096,
		"title" : "매화반점",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/ppqEKXEJ_f",
		"status" : 1
	},
	{
		"idx" : 2097,
		"title" : "로니로티",
		"score" : "3.6",
		"region" : "광진구",
		"url" : "https://www.mangoplate.com/restaurants/_UpyrIiRXF",
		"status" : 1
	},
	{
		"idx" : 2098,
		"title" : "플롭",
		"score" : "3.9",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/hRxG1GICPwm0",
		"status" : 1
	},
	{
		"idx" : 2099,
		"title" : "1인1잔",
		"score" : "3.9",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/AqY6eKJFCfJO",
		"status" : 1
	},
	{
		"idx" : 2100,
		"title" : "휴식",
		"score" : "3.9",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/NrJTOi8MccrB",
		"status" : 1
	},
	{
		"idx" : 2101,
		"title" : "니하오",
		"score" : "3.9",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/i4IbCYrqwDeQ",
		"status" : 1
	},
	{
		"idx" : 2102,
		"title" : "삼오순대국",
		"score" : "3.9",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/IH9yXPcXK9",
		"status" : 1
	},
	{
		"idx" : 2103,
		"title" : "flot",
		"score" : "3.9",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/ajYp-BwKSLvI",
		"status" : 1
	},
	{
		"idx" : 2104,
		"title" : "서부감자국",
		"score" : "3.9",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/Nynzgw4TxE",
		"status" : 1
	},
	{
		"idx" : 2105,
		"title" : "아리산채",
		"score" : "3.9",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/bF5DxqlL2Pg-",
		"status" : 1
	},
	{
		"idx" : 2106,
		"title" : "떡산",
		"score" : "3.9",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/alMgGrweRQ6O",
		"status" : 1
	},
	{
		"idx" : 2107,
		"title" : "오레노라멘",
		"score" : "3.9",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/OSyIG-aiK2u_",
		"status" : 1
	},
	{
		"idx" : 2108,
		"title" : "만포면옥",
		"score" : "3.8",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/magEaA-1UV",
		"status" : 1
	},
	{
		"idx" : 2109,
		"title" : "마산집",
		"score" : "3.8",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/-YAA9JK8sz8h",
		"status" : 1
	},
	{
		"idx" : 2110,
		"title" : "온도차",
		"score" : "3.8",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/ZU5yw9Q_SAu1",
		"status" : 1
	},
	{
		"idx" : 2111,
		"title" : "해례커피",
		"score" : "3.8",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/wRHJbV8y_nrS",
		"status" : 1
	},
	{
		"idx" : 2112,
		"title" : "진김밥",
		"score" : "3.8",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/AV_4WSYDYfZu",
		"status" : 1
	},
	{
		"idx" : 2113,
		"title" : "연어가게",
		"score" : "3.8",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/764IR6DhI1pD",
		"status" : 1
	},
	{
		"idx" : 2114,
		"title" : "불광우동",
		"score" : "3.8",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/w9D_FFL-6-q7",
		"status" : 1
	},
	{
		"idx" : 2115,
		"title" : "원조두꺼비불오징어",
		"score" : "3.7",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/i2Wsu9MZl9",
		"status" : 1
	},
	{
		"idx" : 2116,
		"title" : "옥토끼 제면소",
		"score" : "3.7",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/PAlyyF6Vflt6",
		"status" : 1
	},
	{
		"idx" : 2117,
		"title" : "요요미",
		"score" : "3.7",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/2EBc5FYOtg",
		"status" : 1
	},
	{
		"idx" : 2118,
		"title" : "이병태함흥냉면",
		"score" : "3.7",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/77czWlFgO8Wg",
		"status" : 1
	},
	{
		"idx" : 2119,
		"title" : "허니돈",
		"score" : "3.7",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/5gRwjL-D8B",
		"status" : 1
	},
	{
		"idx" : 2120,
		"title" : "개풍반점",
		"score" : "3.6",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/G7aOvyY70oK0",
		"status" : 1
	},
	{
		"idx" : 2121,
		"title" : "중화원",
		"score" : "3.6",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/mGfG4xsDAn",
		"status" : 1
	},
	{
		"idx" : 2122,
		"title" : "카페볼가심",
		"score" : "3.6",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/3b-K8dfVIHIJ",
		"status" : 1
	},
	{
		"idx" : 2123,
		"title" : "근린커피",
		"score" : "3.6",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/PGNTnW7zhArh",
		"status" : 1
	},
	{
		"idx" : 2124,
		"title" : "세이지",
		"score" : "3.5",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/28BiQn5BV2Vq",
		"status" : 1
	},
	{
		"idx" : 2125,
		"title" : "H3 비스트로",
		"score" : "3.5",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/0tIQPyjIoz",
		"status" : 1
	},
	{
		"idx" : 2126,
		"title" : "갈현동떡볶이",
		"score" : "3.5",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/rTZNpB_M-pfd",
		"status" : 1
	},
	{
		"idx" : 2127,
		"title" : "목노집",
		"score" : "3.5",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/nsC2gslUeJ",
		"status" : 1
	},
	{
		"idx" : 2128,
		"title" : "연어로8길",
		"score" : "3.4",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/9ZYJEykoW0qY",
		"status" : 1
	},
	{
		"idx" : 2129,
		"title" : "플럽커피",
		"score" : "3.4",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/a3_ezzHB0oV-",
		"status" : 1
	},
	{
		"idx" : 2130,
		"title" : "갈현시장할머니떡볶이",
		"score" : "3.4",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/UZQqhBCvX5",
		"status" : 1
	},
	{
		"idx" : 2131,
		"title" : "유라쿠",
		"score" : "3.3",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/pBMxIHywUe",
		"status" : 1
	},
	{
		"idx" : 2132,
		"title" : "롱브레드",
		"score" : "3.3",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/iD1elPW-ojj8",
		"status" : 1
	},
	{
		"idx" : 2133,
		"title" : "통나무집",
		"score" : "3.3",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/dqpcMKkiep",
		"status" : 1
	},
	{
		"idx" : 2134,
		"title" : "뚜띠쿠치나",
		"score" : "3.2",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/EfOphcrypD",
		"status" : 1
	},
	{
		"idx" : 2135,
		"title" : "스시온도",
		"score" : "4.4",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/jvvfFG9jSP1O",
		"status" : 1
	},
	{
		"idx" : 2136,
		"title" : "페스카",
		"score" : "4.3",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/3CzMKMh6pj8B",
		"status" : 1
	},
	{
		"idx" : 2137,
		"title" : "제주도그릴특상",
		"score" : "4.3",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/cHYhGejaT_",
		"status" : 1
	},
	{
		"idx" : 2138,
		"title" : "중국음식점 / 中国小吃",
		"score" : "4.3",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/_otteX1fye-p",
		"status" : 1
	},
	{
		"idx" : 2139,
		"title" : "스시이마",
		"score" : "4.2",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/B64oLGvWbo5d",
		"status" : 1
	},
	{
		"idx" : 2140,
		"title" : "티그레서울",
		"score" : "4.2",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/49EBSxN2tAzG",
		"status" : 1
	},
	{
		"idx" : 2141,
		"title" : "참새식당 스즈메",
		"score" : "4.2",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/b6OJkTL8BxP3",
		"status" : 1
	},
	{
		"idx" : 2142,
		"title" : "YM에스프레소룸",
		"score" : "4.2",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/r0oHu19ooXxW",
		"status" : 1
	},
	{
		"idx" : 2143,
		"title" : "횟집울릉도",
		"score" : "4.2",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/_c641YCsJWU3",
		"status" : 1
	},
	{
		"idx" : 2144,
		"title" : "다온상회",
		"score" : "4.2",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/v3XLx5ImAoY2",
		"status" : 1
	},
	{
		"idx" : 2145,
		"title" : "금원함흥냉면",
		"score" : "4.1",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/RLwmEULwZPHo",
		"status" : 1
	},
	{
		"idx" : 2146,
		"title" : "넙딱집",
		"score" : "4.1",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/o8y9ycADL-oh",
		"status" : 1
	},
	{
		"idx" : 2147,
		"title" : "포옹싸",
		"score" : "4.1",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/2BvZsuhVXBiA",
		"status" : 1
	},
	{
		"idx" : 2148,
		"title" : "일로",
		"score" : "4.1",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/Ht9Zk87oONOS",
		"status" : 1
	},
	{
		"idx" : 2149,
		"title" : "필구커피",
		"score" : "4.1",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/VdkLLgPWWaCe",
		"status" : 1
	},
	{
		"idx" : 2150,
		"title" : "파술타",
		"score" : "4.1",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/e6y6dUIc6YAc",
		"status" : 1
	},
	{
		"idx" : 2151,
		"title" : "스시쇼부",
		"score" : "4.0",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/mbVBPpuvzrdj",
		"status" : 1
	},
	{
		"idx" : 2152,
		"title" : "YM커피하우스",
		"score" : "4.0",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/KZv5teqNeKDa",
		"status" : 1
	},
	{
		"idx" : 2153,
		"title" : "히카리우동",
		"score" : "4.0",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/OybhNJprdbjV",
		"status" : 1
	},
	{
		"idx" : 2154,
		"title" : "마마수제만두",
		"score" : "3.9",
		"region" : "은평구",
		"url" : "https://www.mangoplate.com/restaurants/blRgWC8jCx",
		"status" : 1
	},
	{
		"idx" : 2155,
		"title" : "메노",
		"score" : "4.7",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/ETJ3OloLwEi0",
		"status" : 1
	},
	{
		"idx" : 2156,
		"title" : "홋카이도부타동스미레",
		"score" : "4.6",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/idX28AJjHfRk",
		"status" : 1
	},
	{
		"idx" : 2157,
		"title" : "센트그릴 BBQ",
		"score" : "4.6",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/2VOilscH0DfF",
		"status" : 1
	},
	{
		"idx" : 2158,
		"title" : "연희미식",
		"score" : "4.6",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/nie2d4skIs43",
		"status" : 1
	},
	{
		"idx" : 2159,
		"title" : "안테이쿠",
		"score" : "4.6",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/z5K6C-WFgw7c",
		"status" : 1
	},
	{
		"idx" : 2160,
		"title" : "올레무스",
		"score" : "4.5",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/UUI1cGLPTeBV",
		"status" : 1
	},
	{
		"idx" : 2161,
		"title" : "락희안",
		"score" : "4.5",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/kEfOOVzOe9",
		"status" : 1
	},
	{
		"idx" : 2162,
		"title" : "다이닝후",
		"score" : "4.5",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/LfAgoAQl_SZK",
		"status" : 1
	},
	{
		"idx" : 2163,
		"title" : "롱보트스모커",
		"score" : "4.5",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/4TE2-kRKC1Nm",
		"status" : 1
	},
	{
		"idx" : 2164,
		"title" : "르솔레이",
		"score" : "4.4",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/1yKTH5IUp-bE",
		"status" : 1
	},
	{
		"idx" : 2165,
		"title" : "스탠바이키친",
		"score" : "4.4",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Ct7GYnLL-4z4",
		"status" : 1
	},
	{
		"idx" : 2166,
		"title" : "천진분식",
		"score" : "4.4",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/At5HxAIOYwzS",
		"status" : 1
	},
	{
		"idx" : 2167,
		"title" : "녹원쌈밥",
		"score" : "4.4",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/R4zYqZhSy1",
		"status" : 1
	},
	{
		"idx" : 2168,
		"title" : "책바",
		"score" : "4.4",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Pr6oe1kySMva",
		"status" : 1
	},
	{
		"idx" : 2169,
		"title" : "정리의밤",
		"score" : "4.4",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/YtAUZ2Jgvk1z",
		"status" : 1
	},
	{
		"idx" : 2170,
		"title" : "떼뮤즐렛",
		"score" : "4.4",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/BiQZ9Z9tNLIR",
		"status" : 1
	},
	{
		"idx" : 2171,
		"title" : "미스터서왕만두",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Uq3uakGOVd",
		"status" : 1
	},
	{
		"idx" : 2172,
		"title" : "맘맘테이블",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/whIXrS1NrM_N",
		"status" : 1
	},
	{
		"idx" : 2173,
		"title" : "카라멘야",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/_GV7c9QoRXHT",
		"status" : 1
	},
	{
		"idx" : 2174,
		"title" : "까이식당",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/GvZWLg7ps9w_",
		"status" : 1
	},
	{
		"idx" : 2175,
		"title" : "만동제과",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/xx7zXeY1-3Gg",
		"status" : 1
	},
	{
		"idx" : 2176,
		"title" : "우동카덴",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/HmKQZLRh7P5u",
		"status" : 1
	},
	{
		"idx" : 2177,
		"title" : "에브리띵베이글",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/iEwritUMHuFE",
		"status" : 1
	},
	{
		"idx" : 2178,
		"title" : "프로토콜",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/P6JpThwq_M5R",
		"status" : 1
	},
	{
		"idx" : 2179,
		"title" : "길상양꼬치",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/QsBxSFbx6G",
		"status" : 1
	},
	{
		"idx" : 2180,
		"title" : "담산",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/HpbGe61Wn2T9",
		"status" : 1
	},
	{
		"idx" : 2181,
		"title" : "쿳사",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/U0VgpPrSIDPw",
		"status" : 1
	},
	{
		"idx" : 2182,
		"title" : "영미김밥",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/vipX6WCZbJ8z",
		"status" : 1
	},
	{
		"idx" : 2183,
		"title" : "북성해장국",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/zmG9ebKE7WZV",
		"status" : 1
	},
	{
		"idx" : 2184,
		"title" : "폴앤폴리나",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Tw3mq1lxwDCh",
		"status" : 1
	},
	{
		"idx" : 2185,
		"title" : "Thursday Stuffing",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/nM_OY-xqhdkO",
		"status" : 1
	},
	{
		"idx" : 2186,
		"title" : "바코드",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/9Ldy8KHLdfJz",
		"status" : 1
	},
	{
		"idx" : 2187,
		"title" : "양밍산",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/o6yByqYwtJvs",
		"status" : 1
	},
	{
		"idx" : 2188,
		"title" : "아콘스톨",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/HOmLPakSGyvv",
		"status" : 1
	},
	{
		"idx" : 2189,
		"title" : "탭스터",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/3W-ynjQyeBn6",
		"status" : 1
	},
	{
		"idx" : 2190,
		"title" : "글루글루",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/fIauHvWh7UlO",
		"status" : 1
	},
	{
		"idx" : 2191,
		"title" : "화명당마라탕",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/OpjAAEbdk6yH",
		"status" : 1
	},
	{
		"idx" : 2192,
		"title" : "희로",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/pwGXVoNaIiVw",
		"status" : 1
	},
	{
		"idx" : 2193,
		"title" : "연희단팥죽",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/m0mx1pKOCUY_",
		"status" : 1
	},
	{
		"idx" : 2194,
		"title" : "제주도그릴",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/-tn18cqIMn",
		"status" : 1
	},
	{
		"idx" : 2195,
		"title" : "커피가게동경",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/1qy4udIWtU6h",
		"status" : 1
	},
	{
		"idx" : 2196,
		"title" : "코블러 연희",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/S5AuAWLVUCT1",
		"status" : 1
	},
	{
		"idx" : 2197,
		"title" : "송아저씨빈대떡",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/rN5lnq1jq1",
		"status" : 1
	},
	{
		"idx" : 2198,
		"title" : "연희동양꼬치",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/5_L5Z-vwGHnI",
		"status" : 1
	},
	{
		"idx" : 2199,
		"title" : "진돈부리",
		"score" : "4.3",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/ZkyfihBbiQuf",
		"status" : 1
	},
	{
		"idx" : 2200,
		"title" : "파올로데마리아",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/qOFEcVwF2B",
		"status" : 1
	},
	{
		"idx" : 2201,
		"title" : "한림돈가",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/OTow36IveRkK",
		"status" : 1
	},
	{
		"idx" : 2202,
		"title" : "티앙팡오후의홍차",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/zHeV7AfPBr",
		"status" : 1
	},
	{
		"idx" : 2203,
		"title" : "비아 메렝게",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/6HtLSXhL9JXX",
		"status" : 1
	},
	{
		"idx" : 2204,
		"title" : "가타쯔무리",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/eI6DHlOLb6",
		"status" : 1
	},
	{
		"idx" : 2205,
		"title" : "고삼이",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/xRS2Fzhelv",
		"status" : 1
	},
	{
		"idx" : 2206,
		"title" : "위드미치코",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/fvA4SbtNcpuV",
		"status" : 1
	},
	{
		"idx" : 2207,
		"title" : "온고 파티세리",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/s3xndgYctGuX",
		"status" : 1
	},
	{
		"idx" : 2208,
		"title" : "스웨이커피스테이션",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/x09JLn_dUh5o",
		"status" : 1
	},
	{
		"idx" : 2209,
		"title" : "뉴타운",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/w8C71rPEoR7d",
		"status" : 1
	},
	{
		"idx" : 2210,
		"title" : "링키지버거",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/0qMeHTQX_2Jz",
		"status" : 1
	},
	{
		"idx" : 2211,
		"title" : "맛있는집",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/CVKilsuODr9f",
		"status" : 1
	},
	{
		"idx" : 2212,
		"title" : "고바우집",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/2rz3hTqRTl",
		"status" : 1
	},
	{
		"idx" : 2213,
		"title" : "그로어스",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/qQrx7Yw4juZu",
		"status" : 1
	},
	{
		"idx" : 2214,
		"title" : "월순철판동태찜",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/eKnDZF2Kjj",
		"status" : 1
	},
	{
		"idx" : 2215,
		"title" : "연남장",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/nvlWSgurDGyD",
		"status" : 1
	},
	{
		"idx" : 2216,
		"title" : "심플리키친",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/ilsy-wzug3mE",
		"status" : 1
	},
	{
		"idx" : 2217,
		"title" : "가미분식",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/IMdwWBWbzO",
		"status" : 1
	},
	{
		"idx" : 2218,
		"title" : "고기창고",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/sT8pQXrFwB",
		"status" : 1
	},
	{
		"idx" : 2219,
		"title" : "아이덴티티커피랩",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/BjBqhTW_mUx-",
		"status" : 1
	},
	{
		"idx" : 2220,
		"title" : "신흥떡볶이",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/azhKIPiJy3",
		"status" : 1
	},
	{
		"idx" : 2221,
		"title" : "아바이왕순대",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/NyqsHMGL6vNq",
		"status" : 1
	},
	{
		"idx" : 2222,
		"title" : "서대문족발",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Ixyaq-kpXx",
		"status" : 1
	},
	{
		"idx" : 2223,
		"title" : "연어초밥",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/JOFnCsR3fyop",
		"status" : 1
	},
	{
		"idx" : 2224,
		"title" : "연희동국화빵",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/aAY8kqspy_GT",
		"status" : 1
	},
	{
		"idx" : 2225,
		"title" : "엔타로커피",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/NvBl2wyZrqif",
		"status" : 1
	},
	{
		"idx" : 2226,
		"title" : "한창희천하일면",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/eo2lbjvhIM7a",
		"status" : 1
	},
	{
		"idx" : 2227,
		"title" : "혹스턴",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/0wnvNJa15P1a",
		"status" : 1
	},
	{
		"idx" : 2228,
		"title" : "대명꼬기",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/yAujfN6_mBoq",
		"status" : 1
	},
	{
		"idx" : 2229,
		"title" : "사장님돈까스",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/jm5EPdBzgUcA",
		"status" : 1
	},
	{
		"idx" : 2230,
		"title" : "타오마라탕",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/UFUeKPaXF-pa",
		"status" : 1
	},
	{
		"idx" : 2231,
		"title" : "파이홀",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/97bChF9oJ_",
		"status" : 1
	},
	{
		"idx" : 2232,
		"title" : "그릭데이",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Llyas8qk-8gA",
		"status" : 1
	},
	{
		"idx" : 2233,
		"title" : "정육면체",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/LPWUY_IQ5fFg",
		"status" : 1
	},
	{
		"idx" : 2234,
		"title" : "란주탕슉",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/BZB8LfFQkX",
		"status" : 1
	},
	{
		"idx" : 2235,
		"title" : "컬러드빈",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/hjJXTulMrvtu",
		"status" : 1
	},
	{
		"idx" : 2236,
		"title" : "탐복",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/YOBChdFFpUTg",
		"status" : 1
	},
	{
		"idx" : 2237,
		"title" : "바틸트",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Ig-deF5Fs8",
		"status" : 1
	},
	{
		"idx" : 2238,
		"title" : "가례원",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/j3VFNOMIv0",
		"status" : 1
	},
	{
		"idx" : 2239,
		"title" : "챙스베리",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/VqWX474CoR2o",
		"status" : 1
	},
	{
		"idx" : 2240,
		"title" : "배바위양곱창",
		"score" : "4.2",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/xxB3JOZ8H6hl",
		"status" : 1
	},
	{
		"idx" : 2241,
		"title" : "목란",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/ZtbAGS39Bx",
		"status" : 1
	},
	{
		"idx" : 2242,
		"title" : "마우디",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/v9RYpd8rRQpW",
		"status" : 1
	},
	{
		"idx" : 2243,
		"title" : "라구식당",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/YTzydktWz3",
		"status" : 1
	},
	{
		"idx" : 2244,
		"title" : "타코로코",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/-3qMFUFrZW",
		"status" : 1
	},
	{
		"idx" : 2245,
		"title" : "야바이",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/ynR1RNc1xI",
		"status" : 1
	},
	{
		"idx" : 2246,
		"title" : "방콕익스프레스",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/LjOrjnptTH",
		"status" : 1
	},
	{
		"idx" : 2247,
		"title" : "호밀밭",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/uzBwbTsLla",
		"status" : 1
	},
	{
		"idx" : 2248,
		"title" : "삭",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/pwr58Q2Sxb",
		"status" : 1
	},
	{
		"idx" : 2249,
		"title" : "솔리드웍스",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/_RTL3ImhVo",
		"status" : 1
	},
	{
		"idx" : 2250,
		"title" : "앤트러사이트",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/UAeJb2ECPQbp",
		"status" : 1
	},
	{
		"idx" : 2251,
		"title" : "알레스구떼",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/p9EX5evjI1Fy",
		"status" : 1
	},
	{
		"idx" : 2252,
		"title" : "타코몽",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/dsp5TVaB2X",
		"status" : 1
	},
	{
		"idx" : 2253,
		"title" : "크래프트비어칸",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/bGPsf3o4dh",
		"status" : 1
	},
	{
		"idx" : 2254,
		"title" : "미도 매운향솥",
		"score" : "4.1",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Od0TXYkWCa0P",
		"status" : 1
	},
	{
		"idx" : 2255,
		"title" : "프레퍼스다이어트푸드",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/ZYEr_WGTo3BD",
		"status" : 1
	},
	{
		"idx" : 2256,
		"title" : "주재근베이커리",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/IdFp6IrnNN",
		"status" : 1
	},
	{
		"idx" : 2257,
		"title" : "신촌양꼬치",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Ixvbl7GFTa",
		"status" : 1
	},
	{
		"idx" : 2258,
		"title" : "잭슨피자",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/DvxScNPIF6Th",
		"status" : 1
	},
	{
		"idx" : 2259,
		"title" : "부탄츄",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/jXzOHlVIwY",
		"status" : 1
	},
	{
		"idx" : 2260,
		"title" : "위샐러듀",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/a54ahQ1t0s",
		"status" : 1
	},
	{
		"idx" : 2261,
		"title" : "여우골초밥",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/hBrxSlZnJI",
		"status" : 1
	},
	{
		"idx" : 2262,
		"title" : "소담식당",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/sSesybo-5YeB",
		"status" : 1
	},
	{
		"idx" : 2263,
		"title" : "카페페라",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/WRldRN_Agj",
		"status" : 1
	},
	{
		"idx" : 2264,
		"title" : "피터팬 1978",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/h0V0_07Emn",
		"status" : 1
	},
	{
		"idx" : 2265,
		"title" : "비아37",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/FSMj1IAW4I",
		"status" : 1
	},
	{
		"idx" : 2266,
		"title" : "기꾸스시",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/V7jc9m7i7L",
		"status" : 1
	},
	{
		"idx" : 2267,
		"title" : "탕화쿵부",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/21VBksFMF8yK",
		"status" : 1
	},
	{
		"idx" : 2268,
		"title" : "텐조",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/5sQxyVYnzV9a",
		"status" : 1
	},
	{
		"idx" : 2269,
		"title" : "청송함흥냉면",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/a3o_Mn2UOU",
		"status" : 1
	},
	{
		"idx" : 2270,
		"title" : "미분당",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/NXNrCE6uhsbQ",
		"status" : 1
	},
	{
		"idx" : 2271,
		"title" : "뱅센느",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/cZ0JiPSdBg",
		"status" : 1
	},
	{
		"idx" : 2272,
		"title" : "통큰갈비",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/dC4VJF2T5M",
		"status" : 1
	},
	{
		"idx" : 2273,
		"title" : "연희김밥",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/rcgT8cUDNF",
		"status" : 1
	},
	{
		"idx" : 2274,
		"title" : "씽킹인사이드더박스",
		"score" : "3.8",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/IKAj2lpuVx",
		"status" : 1
	},
	{
		"idx" : 2275,
		"title" : "1987피자",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/lFkqPzkxAdEs",
		"status" : 1
	},
	{
		"idx" : 2276,
		"title" : "돈불1971",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/mZqKGSKHP3",
		"status" : 1
	},
	{
		"idx" : 2277,
		"title" : "파파브레드",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/8TstPEfStzVW",
		"status" : 1
	},
	{
		"idx" : 2278,
		"title" : "문베어",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/7swmgkaQ25zk",
		"status" : 1
	},
	{
		"idx" : 2279,
		"title" : "너스레",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/yLDj8_SS1v",
		"status" : 1
	},
	{
		"idx" : 2280,
		"title" : "경성팥집옥루몽",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/vZUR2JUcLx",
		"status" : 1
	},
	{
		"idx" : 2281,
		"title" : "스튜디오웝",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/YbR-KHVzMd3r",
		"status" : 1
	},
	{
		"idx" : 2282,
		"title" : "딴따라독두공방",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/W6Peu8SwB1Tc",
		"status" : 1
	},
	{
		"idx" : 2283,
		"title" : "플릭온커피",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/ojASbIuvf4sd",
		"status" : 1
	},
	{
		"idx" : 2284,
		"title" : "더 풍년",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/xREheBCZ-HjY",
		"status" : 1
	},
	{
		"idx" : 2285,
		"title" : "파가니니",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/HRPIEO9A9M",
		"status" : 1
	},
	{
		"idx" : 2286,
		"title" : "파티오",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Ub6wmnuoEQ",
		"status" : 1
	},
	{
		"idx" : 2287,
		"title" : "만냥하우스",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/sU3Hu0WdMzdN",
		"status" : 1
	},
	{
		"idx" : 2288,
		"title" : "고래고래",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/D5JU4CgXVKml",
		"status" : 1
	},
	{
		"idx" : 2289,
		"title" : "에뚜왈",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/FYEtdjxCMeUp",
		"status" : 1
	},
	{
		"idx" : 2290,
		"title" : "요릿집",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/dgTYutnfzVAK",
		"status" : 1
	},
	{
		"idx" : 2291,
		"title" : "공드린",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/p4lPlTaYjRWY",
		"status" : 1
	},
	{
		"idx" : 2292,
		"title" : "야채를담다",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/rnfo6EHxgm99",
		"status" : 1
	},
	{
		"idx" : 2293,
		"title" : "육회본가",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/wMi_4F8uCjjp",
		"status" : 1
	},
	{
		"idx" : 2294,
		"title" : "더도이축산직영점",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/O7Esu-Fi_k5h",
		"status" : 1
	},
	{
		"idx" : 2295,
		"title" : "소신이쏘",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/pXrcny4sHv",
		"status" : 1
	},
	{
		"idx" : 2296,
		"title" : "매뉴팩트커피",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/LseZO3K40L",
		"status" : 1
	},
	{
		"idx" : 2297,
		"title" : "와플잇업",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Eixej_2sql",
		"status" : 1
	},
	{
		"idx" : 2298,
		"title" : "마더린러베이글",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/XPZ77GYo-ei8",
		"status" : 1
	},
	{
		"idx" : 2299,
		"title" : "이품",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/lftvwx0k6T",
		"status" : 1
	},
	{
		"idx" : 2300,
		"title" : "에노테카오토",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/4CJinBHlqU",
		"status" : 1
	},
	{
		"idx" : 2301,
		"title" : "대포찜닭",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/t8oS39DrKA",
		"status" : 1
	},
	{
		"idx" : 2302,
		"title" : "오향만두",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/ews_9XqL8v",
		"status" : 1
	},
	{
		"idx" : 2303,
		"title" : "리히트케이크",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/PP7uVrd9KU",
		"status" : 1
	},
	{
		"idx" : 2304,
		"title" : "비밀",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/2jbK-LWJXVs0",
		"status" : 1
	},
	{
		"idx" : 2305,
		"title" : "로드샌드위치",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/sViTwtqkhf",
		"status" : 1
	},
	{
		"idx" : 2306,
		"title" : "키친31",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/ulKeg0GOcc",
		"status" : 1
	},
	{
		"idx" : 2307,
		"title" : "진미",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/MsKIqPAql4Uw",
		"status" : 1
	},
	{
		"idx" : 2308,
		"title" : "유야케도쿄",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/pAdj8mk9or_q",
		"status" : 1
	},
	{
		"idx" : 2309,
		"title" : "타이완소야",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/KTNu62QjmDgC",
		"status" : 1
	},
	{
		"idx" : 2310,
		"title" : "고래파스타",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/DKefidQ_g9T8",
		"status" : 1
	},
	{
		"idx" : 2311,
		"title" : "디폴트벨류",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/0KurhNm-iJHf",
		"status" : 1
	},
	{
		"idx" : 2312,
		"title" : "닭내장집",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/l_oGREfCSM7O",
		"status" : 1
	},
	{
		"idx" : 2313,
		"title" : "칼",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/pt9IBcu9ov",
		"status" : 1
	},
	{
		"idx" : 2314,
		"title" : "라이프커피컴퍼니",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/SAAbUFhuNV3c",
		"status" : 1
	},
	{
		"idx" : 2315,
		"title" : "보울룸",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/0MO4j1w27-Eq",
		"status" : 1
	},
	{
		"idx" : 2316,
		"title" : "ANNIV",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/8JtaPRvAbAw5",
		"status" : 1
	},
	{
		"idx" : 2317,
		"title" : "유자유김치떡볶이",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/7AQQjubOs6fk",
		"status" : 1
	},
	{
		"idx" : 2318,
		"title" : "피터팬",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/TfO4LIvtPE",
		"status" : 1
	},
	{
		"idx" : 2319,
		"title" : "통통돼지",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Ktb3StHRgf",
		"status" : 1
	},
	{
		"idx" : 2320,
		"title" : "원앤온리커피",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/oyMdU1Wc64Js",
		"status" : 1
	},
	{
		"idx" : 2321,
		"title" : "하이파이",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/rDCNBSO0GZ5l",
		"status" : 1
	},
	{
		"idx" : 2322,
		"title" : "Mr Lee",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/bXXcUlcIIrRf",
		"status" : 1
	},
	{
		"idx" : 2323,
		"title" : "홍대삭",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/QY6cyCiIBg",
		"status" : 1
	},
	{
		"idx" : 2324,
		"title" : "호천식당",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/FDOMyDoHi8Nr",
		"status" : 1
	},
	{
		"idx" : 2325,
		"title" : "엄마식탁",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/h6euo7kXywd3",
		"status" : 1
	},
	{
		"idx" : 2326,
		"title" : "유소바",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/sHr8P_jBrBFM",
		"status" : 1
	},
	{
		"idx" : 2327,
		"title" : "룩백커피",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/y-Jyd6G0_IAw",
		"status" : 1
	},
	{
		"idx" : 2328,
		"title" : "TMOON",
		"score" : "4.0",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/EH41y2_eFnDy",
		"status" : 1
	},
	{
		"idx" : 2329,
		"title" : "클로리스",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/h-AO9uicoz",
		"status" : 1
	},
	{
		"idx" : 2330,
		"title" : "독수리다방",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/t7cH4kv6-M",
		"status" : 1
	},
	{
		"idx" : 2331,
		"title" : "완차이",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/YQ6w_FseaC",
		"status" : 1
	},
	{
		"idx" : 2332,
		"title" : "또보겠지떡볶이집",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/N1m3BEqXQ1",
		"status" : 1
	},
	{
		"idx" : 2333,
		"title" : "초코블로썸",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/7O8qMLGBEJ",
		"status" : 1
	},
	{
		"idx" : 2334,
		"title" : "가마마루이라멘",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/3WQEVWeZnk",
		"status" : 1
	},
	{
		"idx" : 2335,
		"title" : "공복식당",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/2ocQLDe_fHEj",
		"status" : 1
	},
	{
		"idx" : 2336,
		"title" : "조선의육개장",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/yPqj7srpHe",
		"status" : 1
	},
	{
		"idx" : 2337,
		"title" : "제니스카페",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/zdU04cuf9N",
		"status" : 1
	},
	{
		"idx" : 2338,
		"title" : "콜드레시피",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/DfV3DNmi9h",
		"status" : 1
	},
	{
		"idx" : 2339,
		"title" : "금옥당",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/aabTSSTTuPO7",
		"status" : 1
	},
	{
		"idx" : 2340,
		"title" : "컨시어지 커피",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/LKE4ycSOaEnd",
		"status" : 1
	},
	{
		"idx" : 2341,
		"title" : "독립문맛집",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/mZMBf3Ti5Wmw",
		"status" : 1
	},
	{
		"idx" : 2342,
		"title" : "편의방",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/fNbvMFLVKP",
		"status" : 1
	},
	{
		"idx" : 2343,
		"title" : "원즈오운베이커리",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/Du612RD7ci61",
		"status" : 1
	},
	{
		"idx" : 2344,
		"title" : "노아스로스팅",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/flHytk0jIT",
		"status" : 1
	},
	{
		"idx" : 2345,
		"title" : "피망과토마토",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/mFwQU3LTXBze",
		"status" : 1
	},
	{
		"idx" : 2346,
		"title" : "푸어링아웃",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/B_BEDn3j05HC",
		"status" : 1
	},
	{
		"idx" : 2347,
		"title" : "아건",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/0P2lXS1izr",
		"status" : 1
	},
	{
		"idx" : 2348,
		"title" : "벽제갈비",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/-UrEMfQ2UM",
		"status" : 1
	},
	{
		"idx" : 2349,
		"title" : "옐로우보울",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/jcaMykd0aP3V",
		"status" : 1
	},
	{
		"idx" : 2350,
		"title" : "유닭스토리 닭한마리",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/o6kRxAJtAN",
		"status" : 1
	},
	{
		"idx" : 2351,
		"title" : "벨라프라하",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/r1O4z-YP4N",
		"status" : 1
	},
	{
		"idx" : 2352,
		"title" : "마이시크릿메이트",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/KaAW320qKi",
		"status" : 1
	},
	{
		"idx" : 2353,
		"title" : "희게",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/YjPmnl0xs1Ev",
		"status" : 1
	},
	{
		"idx" : 2354,
		"title" : "백색소음",
		"score" : "3.9",
		"region" : "서대문구",
		"url" : "https://www.mangoplate.com/restaurants/MfY8n89D5Xvy",
		"status" : 1
	},
	{
		"idx" : 2355,
		"title" : "이남장",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/by3HdSaaxw",
		"status" : 1
	},
	{
		"idx" : 2356,
		"title" : "페닌슐라",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/8wHdXeFWSR",
		"status" : 1
	},
	{
		"idx" : 2357,
		"title" : "서울다이닝",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/lVh6VoN9FyHN",
		"status" : 1
	},
	{
		"idx" : 2358,
		"title" : "가메골손왕만두",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/39q823jdA1",
		"status" : 1
	},
	{
		"idx" : 2359,
		"title" : "콘부",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/ASQDGRn3WA6n",
		"status" : 1
	},
	{
		"idx" : 2360,
		"title" : "국일따로국밥",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/5yc8sn-LpM",
		"status" : 1
	},
	{
		"idx" : 2361,
		"title" : "촛불1978",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/8EriNtQw5e",
		"status" : 1
	},
	{
		"idx" : 2362,
		"title" : "세림",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/dtFPmR-F4PkF",
		"status" : 1
	},
	{
		"idx" : 2363,
		"title" : "페스타바이민구",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/aAbiMiI5URPT",
		"status" : 1
	},
	{
		"idx" : 2364,
		"title" : "을지로양대장",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/qBK5u48j629I",
		"status" : 1
	},
	{
		"idx" : 2365,
		"title" : "초류향",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/tYQpyo--4i",
		"status" : 1
	},
	{
		"idx" : 2366,
		"title" : "벱비엣",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/6CL8lm8a-sTa",
		"status" : 1
	},
	{
		"idx" : 2367,
		"title" : "숙희",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/thz4zQm1UXz3",
		"status" : 1
	},
	{
		"idx" : 2368,
		"title" : "전통맛집",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/xKaylv58jRyW",
		"status" : 1
	},
	{
		"idx" : 2369,
		"title" : "어시장전주식당",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/ug8vaJTZkt",
		"status" : 1
	},
	{
		"idx" : 2370,
		"title" : "쓰리도어즈",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/5epiIcGL6qhD",
		"status" : 1
	},
	{
		"idx" : 2371,
		"title" : "용금옥",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/3psv9YObpM",
		"status" : 1
	},
	{
		"idx" : 2372,
		"title" : "짱구네",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/RnRV7GgnA3",
		"status" : 1
	},
	{
		"idx" : 2373,
		"title" : "온수반",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/ONYfd9WmP4hT",
		"status" : 1
	},
	{
		"idx" : 2374,
		"title" : "뵈르 누아제트",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/8nMxXbAF7t6O",
		"status" : 1
	},
	{
		"idx" : 2375,
		"title" : "진주회관",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/2IpBtf5s2-",
		"status" : 1
	},
	{
		"idx" : 2376,
		"title" : "평양면옥",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/Ae8ggD4u0V",
		"status" : 1
	},
	{
		"idx" : 2377,
		"title" : "필동면옥",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/GsNUSk8aMy",
		"status" : 1
	},
	{
		"idx" : 2378,
		"title" : "더라이브러리",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/NKeKBl9J2p",
		"status" : 1
	},
	{
		"idx" : 2379,
		"title" : "사랑방칼국수",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/HWp4HhRE-7",
		"status" : 1
	},
	{
		"idx" : 2380,
		"title" : "이가네떡볶이",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/SbwyE_ucHe",
		"status" : 1
	},
	{
		"idx" : 2381,
		"title" : "아리아",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/rwXV5GxLCS",
		"status" : 1
	},
	{
		"idx" : 2382,
		"title" : "황평집닭곰탕",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/V6xxv1kC-g",
		"status" : 1
	},
	{
		"idx" : 2383,
		"title" : "광화문국밥",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/adFAd5nyITV0",
		"status" : 1
	},
	{
		"idx" : 2384,
		"title" : "르빵",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/2u7qxiw3lX",
		"status" : 1
	},
	{
		"idx" : 2385,
		"title" : "호수집",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/T_pB9wzaK6",
		"status" : 1
	},
	{
		"idx" : 2386,
		"title" : "은화계",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/pNK2QW5o6fnj",
		"status" : 1
	},
	{
		"idx" : 2387,
		"title" : "주신당",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/mq1ovWy5JEbL",
		"status" : 1
	},
	{
		"idx" : 2388,
		"title" : "다만프레르",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/qKcTCTPwY_VP",
		"status" : 1
	},
	{
		"idx" : 2389,
		"title" : "오장동흥남집",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/IBomQ8pwRY",
		"status" : 1
	},
	{
		"idx" : 2390,
		"title" : "멘텐",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/HyyQTyz7Dj42",
		"status" : 1
	},
	{
		"idx" : 2391,
		"title" : "로스트앤파운드",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/Nq90QweeDgfW",
		"status" : 1
	},
	{
		"idx" : 2392,
		"title" : "부민옥",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/wbnP4WrJWT",
		"status" : 1
	},
	{
		"idx" : 2393,
		"title" : "혼고기",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/LAoka2B8d1PH",
		"status" : 1
	},
	{
		"idx" : 2394,
		"title" : "Karamel",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/PwCiUmXeCd1L",
		"status" : 1
	},
	{
		"idx" : 2395,
		"title" : "오제제",
		"score" : "4.8",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/DOqnqbIeugJI",
		"status" : 1
	},
	{
		"idx" : 2396,
		"title" : "회현식당",
		"score" : "4.7",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/UifwVuxRDTSo",
		"status" : 1
	},
	{
		"idx" : 2397,
		"title" : "패스트리부티크",
		"score" : "4.7",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/aeO_cG35KO",
		"status" : 1
	},
	{
		"idx" : 2398,
		"title" : "팔레드 신",
		"score" : "4.6",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/4Zcp4HYDFaS9",
		"status" : 1
	},
	{
		"idx" : 2399,
		"title" : "유즈라멘",
		"score" : "4.6",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/Do_pQUBxN9-l",
		"status" : 1
	},
	{
		"idx" : 2400,
		"title" : "미성옥",
		"score" : "4.6",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/EzqU3evw9Q",
		"status" : 1
	},
	{
		"idx" : 2401,
		"title" : "시미베",
		"score" : "4.6",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/qKb6AGwIdr7P",
		"status" : 1
	},
	{
		"idx" : 2402,
		"title" : "러시아케익",
		"score" : "4.6",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/dqL32F-fFBqa",
		"status" : 1
	},
	{
		"idx" : 2403,
		"title" : "시키카츠",
		"score" : "4.6",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/y_6f0TYITVa8",
		"status" : 1
	},
	{
		"idx" : 2404,
		"title" : "유가",
		"score" : "4.6",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/PUhlqAGFRpBY",
		"status" : 1
	},
	{
		"idx" : 2405,
		"title" : "풍년 닭도리탕",
		"score" : "4.6",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/zWVgSFqWIQrj",
		"status" : 1
	},
	{
		"idx" : 2406,
		"title" : "동강나루터",
		"score" : "4.6",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/QZoWDJJ1go",
		"status" : 1
	},
	{
		"idx" : 2407,
		"title" : "서울로인",
		"score" : "4.6",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/9BZEDhG2rz6N",
		"status" : 1
	},
	{
		"idx" : 2408,
		"title" : "우래옥",
		"score" : "4.5",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/1pmv75vVQx",
		"status" : 1
	},
	{
		"idx" : 2409,
		"title" : "라망시크레",
		"score" : "4.5",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/ugW7sOel2u88",
		"status" : 1
	},
	{
		"idx" : 2410,
		"title" : "맷차",
		"score" : "4.5",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/PPQahwaSFrhU",
		"status" : 1
	},
	{
		"idx" : 2411,
		"title" : "애성회관 한우곰탕",
		"score" : "4.5",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/8f3EsL0cak",
		"status" : 1
	},
	{
		"idx" : 2412,
		"title" : "리사르커피로스터스",
		"score" : "4.5",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/oTMDQ2Djqd9T",
		"status" : 1
	},
	{
		"idx" : 2413,
		"title" : "홍연",
		"score" : "4.5",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/0hflR8ZCg5",
		"status" : 1
	},
	{
		"idx" : 2414,
		"title" : "해남낙지",
		"score" : "4.5",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/JJe1oXUf6s",
		"status" : 1
	},
	{
		"idx" : 2415,
		"title" : "농민백암순대",
		"score" : "4.5",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/LYBL7h4P6lG4",
		"status" : 1
	},
	{
		"idx" : 2416,
		"title" : "백화양곱창1호",
		"score" : "4.5",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/TRX30sygeHzb",
		"status" : 1
	},
	{
		"idx" : 2417,
		"title" : "아리아께",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/WOnlBsE3wq",
		"status" : 1
	},
	{
		"idx" : 2418,
		"title" : "을지면옥 (휴업중)",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/0eY8YzMwpZ",
		"status" : 1
	},
	{
		"idx" : 2419,
		"title" : "더파크뷰",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/YtI0ysL08J",
		"status" : 1
	},
	{
		"idx" : 2420,
		"title" : "주옥",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/NjGV4odJU65L",
		"status" : 1
	},
	{
		"idx" : 2421,
		"title" : "이재모피자",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/iSH-kv4Shm",
		"status" : 1
	},
	{
		"idx" : 2422,
		"title" : "나인스게이트",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/DemJJ12C1J",
		"status" : 1
	},
	{
		"idx" : 2423,
		"title" : "무교동북어국집",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/lrhqu5J2Kg",
		"status" : 1
	},
	{
		"idx" : 2424,
		"title" : "백송",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/Bj-3OuGXs5G4",
		"status" : 1
	},
	{
		"idx" : 2425,
		"title" : "우육미",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/BKGj7S4wLeUP",
		"status" : 1
	},
	{
		"idx" : 2426,
		"title" : "성심당케익부띠끄",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/xeKYUj_igz",
		"status" : 1
	},
	{
		"idx" : 2427,
		"title" : "도림",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/KWYvFbCbtE",
		"status" : 1
	},
	{
		"idx" : 2428,
		"title" : "디라이프스타일키친",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/iVAHP06TG-ai",
		"status" : 1
	},
	{
		"idx" : 2429,
		"title" : "평안도족발집",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/NhZm791BDVzZ",
		"status" : 1
	},
	{
		"idx" : 2430,
		"title" : "무학",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/Qe4qpFaIVNjY",
		"status" : 1
	},
	{
		"idx" : 2431,
		"title" : "계류관",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/Entd6J5XYyQ8",
		"status" : 1
	},
	{
		"idx" : 2432,
		"title" : "진짜해장국 대화정",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/bpGgQ5lPat",
		"status" : 1
	},
	{
		"idx" : 2433,
		"title" : "제주연탄집",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/d0qJSiT8ESUf",
		"status" : 1
	},
	{
		"idx" : 2434,
		"title" : "디핀",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/qZu91F3o2GJQ",
		"status" : 1
	},
	{
		"idx" : 2435,
		"title" : "신세계떡볶이",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/IfBJCoZpC2",
		"status" : 1
	},
	{
		"idx" : 2436,
		"title" : "전가복",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/PUwudH2BYKJB",
		"status" : 1
	},
	{
		"idx" : 2437,
		"title" : "엘까페씨또바",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/uaSU3I2onfhR",
		"status" : 1
	},
	{
		"idx" : 2438,
		"title" : "도우큐먼트",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/N3tIlIMoX-FJ",
		"status" : 1
	},
	{
		"idx" : 2439,
		"title" : "커피인쇄소",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/rubZTrLPIzJ4",
		"status" : 1
	},
	{
		"idx" : 2440,
		"title" : "무궁화",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/oz7lPAvQQ6",
		"status" : 1
	},
	{
		"idx" : 2441,
		"title" : "나이스타임2",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/cK3cJsP8USlW",
		"status" : 1
	},
	{
		"idx" : 2442,
		"title" : "다동 황소막창",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/woOChljkSNyQ",
		"status" : 1
	},
	{
		"idx" : 2443,
		"title" : "오오토리",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/mAcwnQMBZBWX",
		"status" : 1
	},
	{
		"idx" : 2444,
		"title" : "빌리앤오티스",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/GnBO2ROmBEuF",
		"status" : 1
	},
	{
		"idx" : 2445,
		"title" : "퀸즈베리도넛하우스",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/nNkKGXCVUehG",
		"status" : 1
	},
	{
		"idx" : 2446,
		"title" : "OUSIA PATISSERIE",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/-bRO0aJyITY3",
		"status" : 1
	},
	{
		"idx" : 2447,
		"title" : "홍산",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/rP71smF7ZuLP",
		"status" : 1
	},
	{
		"idx" : 2448,
		"title" : "대원집",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/AsZ5wetEzb",
		"status" : 1
	},
	{
		"idx" : 2449,
		"title" : "레브슈크레",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/Eh1AS2dPB1bb",
		"status" : 1
	},
	{
		"idx" : 2450,
		"title" : "오뗄두스",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/AuKIGMgjMADR",
		"status" : 1
	},
	{
		"idx" : 2451,
		"title" : "피클피클익스프레스",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/Moo14PCPXduT",
		"status" : 1
	},
	{
		"idx" : 2452,
		"title" : "칙피스",
		"score" : "4.4",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/uQhxwxc1HWrI",
		"status" : 1
	},
	{
		"idx" : 2453,
		"title" : "금돼지식당",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/J9i5c2EuAL3w",
		"status" : 1
	},
	{
		"idx" : 2454,
		"title" : "스시조",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/tBo4Hr5boy",
		"status" : 1
	},
	{
		"idx" : 2455,
		"title" : "소공죽집",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/Y1vubJ53sM",
		"status" : 1
	},
	{
		"idx" : 2456,
		"title" : "물꽁식당",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/NoE2FI853a",
		"status" : 1
	},
	{
		"idx" : 2457,
		"title" : "큰기와집한상",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/N21KHNiAlB7p",
		"status" : 1
	},
	{
		"idx" : 2458,
		"title" : "남포당",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/rM9-YgxV-pBF",
		"status" : 1
	},
	{
		"idx" : 2459,
		"title" : "오뗄두스",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/7jfEEPXh_6",
		"status" : 1
	},
	{
		"idx" : 2460,
		"title" : "브레라",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/IIZs0BEGUI",
		"status" : 1
	},
	{
		"idx" : 2461,
		"title" : "이나니와요스케",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/MzXcy6-jr1",
		"status" : 1
	},
	{
		"idx" : 2462,
		"title" : "스담",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/NaNdBaeP9nZS",
		"status" : 1
	},
	{
		"idx" : 2463,
		"title" : "라세느",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/WiJ7WFMBJJ",
		"status" : 1
	},
	{
		"idx" : 2464,
		"title" : "적당",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/u9h0ti1bD6sb",
		"status" : 1
	},
	{
		"idx" : 2465,
		"title" : "동원집",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/lt8hhqZy4E",
		"status" : 1
	},
	{
		"idx" : 2466,
		"title" : "장프리고",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/a31mbFg680OL",
		"status" : 1
	},
	{
		"idx" : 2467,
		"title" : "만족오향족발",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/WdrNAlzTbr",
		"status" : 1
	},
	{
		"idx" : 2468,
		"title" : "붓처스컷",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/Tnn18Fifm8",
		"status" : 1
	},
	{
		"idx" : 2469,
		"title" : "호랑이",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/DawnXcDDLx0C",
		"status" : 1
	},
	{
		"idx" : 2470,
		"title" : "중앙떡볶이",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/PDZ8dBA3Qa",
		"status" : 1
	},
	{
		"idx" : 2471,
		"title" : "금산제면소",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/5okkqUrcyYbr",
		"status" : 1
	},
	{
		"idx" : 2472,
		"title" : "마크 다모르",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/6SzdKW0mKEe8",
		"status" : 1
	},
	{
		"idx" : 2473,
		"title" : "부타이제2막",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/oohKKqt3Tlkh",
		"status" : 1
	},
	{
		"idx" : 2474,
		"title" : "삐삣버거",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/CDGoLWziQj_B",
		"status" : 1
	},
	{
		"idx" : 2475,
		"title" : "차덕분",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/QEv1wVO8L_Dk",
		"status" : 1
	},
	{
		"idx" : 2476,
		"title" : "하동관",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/3yYYpXLNYe",
		"status" : 1
	},
	{
		"idx" : 2477,
		"title" : "무명스키야키",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/f9GNoKFZaLdE",
		"status" : 1
	},
	{
		"idx" : 2478,
		"title" : "하니칼국수",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/7voHWAy3hqrc",
		"status" : 1
	},
	{
		"idx" : 2479,
		"title" : "어라우즈",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/-VwxcDy-Mk0u",
		"status" : 1
	},
	{
		"idx" : 2480,
		"title" : "스시 소우카이",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/avWzo-SN4QLl",
		"status" : 1
	},
	{
		"idx" : 2481,
		"title" : "사마르칸트시티",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/f0QSaYBg5Ri_",
		"status" : 1
	},
	{
		"idx" : 2482,
		"title" : "국수가좋아",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/ryB8ZVrIMfcu",
		"status" : 1
	},
	{
		"idx" : 2483,
		"title" : "할아버지손칼국수",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/iESESNCX3CqA",
		"status" : 1
	},
	{
		"idx" : 2484,
		"title" : "라스칼라",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/sUZdxEUO0kMZ",
		"status" : 1
	},
	{
		"idx" : 2485,
		"title" : "동해막국수",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/W5pIYirB4Q",
		"status" : 1
	},
	{
		"idx" : 2486,
		"title" : "보건옥",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/lNhEzH1mvG",
		"status" : 1
	},
	{
		"idx" : 2487,
		"title" : "라까예",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/EUZp11FCQJq1",
		"status" : 1
	},
	{
		"idx" : 2488,
		"title" : "가쯔야",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/v4olSZq9NS",
		"status" : 1
	},
	{
		"idx" : 2489,
		"title" : "원흥",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/uAjNY4QW79",
		"status" : 1
	},
	{
		"idx" : 2490,
		"title" : "도우대디",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/zrv6vGwVfGWo",
		"status" : 1
	},
	{
		"idx" : 2491,
		"title" : "왕거미식당",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/g4-iA6BJ5o",
		"status" : 1
	},
	{
		"idx" : 2492,
		"title" : "모모상점",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/d594hYy4NS2H",
		"status" : 1
	},
	{
		"idx" : 2493,
		"title" : "처가집",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/6QiDU7H-iu",
		"status" : 1
	},
	{
		"idx" : 2494,
		"title" : "육통령",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/85NoWAaAtb",
		"status" : 1
	},
	{
		"idx" : 2495,
		"title" : "진미네",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/LNL7gn0yq1oE",
		"status" : 1
	},
	{
		"idx" : 2496,
		"title" : "임페리얼트레저",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/1KoxMlQL0NZk",
		"status" : 1
	},
	{
		"idx" : 2497,
		"title" : "진고개",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/i-jRk-wA4y",
		"status" : 1
	},
	{
		"idx" : 2498,
		"title" : "한영식당",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/pXFoF1Ai4j",
		"status" : 1
	},
	{
		"idx" : 2499,
		"title" : "메콩사롱",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/RPHhTXRVrv3I",
		"status" : 1
	},
	{
		"idx" : 2500,
		"title" : "금성관 나주곰탕나주전",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/VxPwOsJProWe",
		"status" : 1
	},
	{
		"idx" : 2501,
		"title" : "을지육점",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/eVnIo8o_F3nU",
		"status" : 1
	},
	{
		"idx" : 2502,
		"title" : "8번식당",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/sy3xMn45aC",
		"status" : 1
	},
	{
		"idx" : 2503,
		"title" : "한가람",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/54a5YPmYKw",
		"status" : 1
	},
	{
		"idx" : 2504,
		"title" : "메이드림",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/jZH7cyUqitwZ",
		"status" : 1
	},
	{
		"idx" : 2505,
		"title" : "만나손칼국수",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/3hEiWEVsAWUn",
		"status" : 1
	},
	{
		"idx" : 2506,
		"title" : "동은성",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/Uj4uZD2gO-",
		"status" : 1
	},
	{
		"idx" : 2507,
		"title" : "포비",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/eTRQjs_QX5Z1",
		"status" : 1
	},
	{
		"idx" : 2508,
		"title" : "펠트커피",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/-XAU9pTDQl24",
		"status" : 1
	},
	{
		"idx" : 2509,
		"title" : "통통김밥",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/qEF_0Bx3dYs0",
		"status" : 1
	},
	{
		"idx" : 2510,
		"title" : "남산미수",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/YMI0tKapz4_C",
		"status" : 1
	},
	{
		"idx" : 2511,
		"title" : "누에하우스",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/2qW7MsR1kcts",
		"status" : 1
	},
	{
		"idx" : 2512,
		"title" : "도향촌",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/tdDEjX3CBRnj",
		"status" : 1
	},
	{
		"idx" : 2513,
		"title" : "영덕회식당",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/DIKinX_Ju3",
		"status" : 1
	},
	{
		"idx" : 2514,
		"title" : "금토일샴페인빠",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/bqj6JGRePCT6",
		"status" : 1
	},
	{
		"idx" : 2515,
		"title" : "대정양곱창",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/uZfoMlez4R",
		"status" : 1
	},
	{
		"idx" : 2516,
		"title" : "중앙갈치식당",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/wGl2LEIvna",
		"status" : 1
	},
	{
		"idx" : 2517,
		"title" : "을지깐깐",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/0V_IOpBnswRk",
		"status" : 1
	},
	{
		"idx" : 2518,
		"title" : "연길반점",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/cw9zRee5jx",
		"status" : 1
	},
	{
		"idx" : 2519,
		"title" : "수와",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/QrWURMyXU63f",
		"status" : 1
	},
	{
		"idx" : 2520,
		"title" : "요우란",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/GoaJ4WEYsFjZ",
		"status" : 1
	},
	{
		"idx" : 2521,
		"title" : "을지다락",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/6NFuxuCbczhZ",
		"status" : 1
	},
	{
		"idx" : 2522,
		"title" : "델리카한스",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/KZMeNQ4ajz",
		"status" : 1
	},
	{
		"idx" : 2523,
		"title" : "하이타이",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/_wGoj3UhP3",
		"status" : 1
	},
	{
		"idx" : 2524,
		"title" : "영양센터",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/vbS60S4HLH",
		"status" : 1
	},
	{
		"idx" : 2525,
		"title" : "막내회집",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/sRtC4Lz3IF",
		"status" : 1
	},
	{
		"idx" : 2526,
		"title" : "중림장설렁탕",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/ckcH8LFJvP",
		"status" : 1
	},
	{
		"idx" : 2527,
		"title" : "동경우동",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/vIekSGD9Q-",
		"status" : 1
	},
	{
		"idx" : 2528,
		"title" : "희락",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/JN9AF0DiVw",
		"status" : 1
	},
	{
		"idx" : 2529,
		"title" : "느티나무설렁탕",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/WZexIRdBp_",
		"status" : 1
	},
	{
		"idx" : 2530,
		"title" : "팔공막창",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/qHKY4o2_-L",
		"status" : 1
	},
	{
		"idx" : 2531,
		"title" : "헤베커피",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/JjAyjuR3wR8n",
		"status" : 1
	},
	{
		"idx" : 2532,
		"title" : "직화장인",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/qN5lFTewIVUo",
		"status" : 1
	},
	{
		"idx" : 2533,
		"title" : "스시사쿠",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/5OkeYMoameE1",
		"status" : 1
	},
	{
		"idx" : 2534,
		"title" : "한암동",
		"score" : "4.1",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/3urn1CZ_jc5w",
		"status" : 1
	},
	{
		"idx" : 2535,
		"title" : "드로우에스프레소바",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/_YSmb3fhv8nV",
		"status" : 1
	},
	{
		"idx" : 2536,
		"title" : "철철복집",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/nEZ0ANW9XK",
		"status" : 1
	},
	{
		"idx" : 2537,
		"title" : "롤러커피",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/vMyConAFK9md",
		"status" : 1
	},
	{
		"idx" : 2538,
		"title" : "라운지 파라다이스",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/8nn69ky6oH44",
		"status" : 1
	},
	{
		"idx" : 2539,
		"title" : "영덕회식당",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/HemADHPVH_",
		"status" : 1
	},
	{
		"idx" : 2540,
		"title" : "조조칼국수",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/SnEmIMSwqafw",
		"status" : 1
	},
	{
		"idx" : 2541,
		"title" : "잉꼬",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/Zw5Yk8083-iW",
		"status" : 1
	},
	{
		"idx" : 2542,
		"title" : "빨간거짱구네",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/28TOno903c-u",
		"status" : 1
	},
	{
		"idx" : 2543,
		"title" : "꾸왁칼국수",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/70OKW4lHh_-X",
		"status" : 1
	},
	{
		"idx" : 2544,
		"title" : "히바리",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/QWKhT_Lwc5OF",
		"status" : 1
	},
	{
		"idx" : 2545,
		"title" : "해마의방",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/sh8w-Ra42flh",
		"status" : 1
	},
	{
		"idx" : 2546,
		"title" : "우동가조쿠",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/u31fdcoLIPwr",
		"status" : 1
	},
	{
		"idx" : 2547,
		"title" : "보스호프",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/kf0nwJhZhy",
		"status" : 1
	},
	{
		"idx" : 2548,
		"title" : "카돈마리",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/18iUl5XlRyR5",
		"status" : 1
	},
	{
		"idx" : 2549,
		"title" : "주토피아",
		"score" : "4.3",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/F3cU_D1Ko8yQ",
		"status" : 1
	},
	{
		"idx" : 2550,
		"title" : "성심당",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/ZjelP9zEEP",
		"status" : 1
	},
	{
		"idx" : 2551,
		"title" : "란주칼면",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/KeZUkxsFMl",
		"status" : 1
	},
	{
		"idx" : 2552,
		"title" : "신승반점",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/ZiIldxQxUr",
		"status" : 1
	},
	{
		"idx" : 2553,
		"title" : "팔선",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/opaFM1XeoG",
		"status" : 1
	},
	{
		"idx" : 2554,
		"title" : "명동교자",
		"score" : "4.2",
		"region" : "중구",
		"url" : "https://www.mangoplate.com/restaurants/E3egARz24E",
		"status" : 1
	},
	{
		"idx" : 2555,
		"title" : "폴앤폴리나",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/jbXHGq3QwY",
		"status" : 1
	},
	{
		"idx" : 2556,
		"title" : "오죽이네",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/58VdLj8nKS",
		"status" : 1
	},
	{
		"idx" : 2557,
		"title" : "물랑",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/DIjlg70h-t",
		"status" : 1
	},
	{
		"idx" : 2558,
		"title" : "찰스에이치",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/wT1_KWIfeZ",
		"status" : 1
	},
	{
		"idx" : 2559,
		"title" : "후니도니",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/KV9lSGa6xNQp",
		"status" : 1
	},
	{
		"idx" : 2560,
		"title" : "백부장집닭한마리",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/kbo6CkIp6d",
		"status" : 1
	},
	{
		"idx" : 2561,
		"title" : "버거파크",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/9pIv7vDY70k1",
		"status" : 1
	},
	{
		"idx" : 2562,
		"title" : "오레노라멘",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/6bp9NtVjCCwL",
		"status" : 1
	},
	{
		"idx" : 2563,
		"title" : "도마유즈라멘",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/kDd7uvQkQJxl",
		"status" : 1
	},
	{
		"idx" : 2564,
		"title" : "수도원",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/l4SRQIFhkEIN",
		"status" : 1
	},
	{
		"idx" : 2565,
		"title" : "혜화도담",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/Yx9sin8OvFy6",
		"status" : 1
	},
	{
		"idx" : 2566,
		"title" : "장수한방삼계탕",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/GMd0yzrobn",
		"status" : 1
	},
	{
		"idx" : 2567,
		"title" : "소금집델리 안국",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/w_u6_cCr0qX0",
		"status" : 1
	},
	{
		"idx" : 2568,
		"title" : "Osso파스타",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/ov0hZAWQZj3J",
		"status" : 1
	},
	{
		"idx" : 2569,
		"title" : "파네트크루아상팩토리",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/-czYKuW77F_5",
		"status" : 1
	},
	{
		"idx" : 2570,
		"title" : "호가양꼬치",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/JjS1bklwYEM6",
		"status" : 1
	},
	{
		"idx" : 2571,
		"title" : "논데",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/CU4KmdWT6g",
		"status" : 1
	},
	{
		"idx" : 2572,
		"title" : "도취",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/UN15dCZIP3Cw",
		"status" : 1
	},
	{
		"idx" : 2573,
		"title" : "부빙",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/B6cFwd-mm2",
		"status" : 1
	},
	{
		"idx" : 2574,
		"title" : "공기식당",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/WX9nij4-rf",
		"status" : 1
	},
	{
		"idx" : 2575,
		"title" : "육회자매집",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/umDMoedGJg",
		"status" : 1
	},
	{
		"idx" : 2576,
		"title" : "김진목삼",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/5vEzVX3xJZ1Y",
		"status" : 1
	},
	{
		"idx" : 2577,
		"title" : "포비브라이트",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/vkE5tx5MgycG",
		"status" : 1
	},
	{
		"idx" : 2578,
		"title" : "톤티커피",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/ORd-o6IEQz0V",
		"status" : 1
	},
	{
		"idx" : 2579,
		"title" : "렁팡스",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/Iav6RUIwPzrH",
		"status" : 1
	},
	{
		"idx" : 2580,
		"title" : "개성철렵",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/xSwUwLVMR2rN",
		"status" : 1
	},
	{
		"idx" : 2581,
		"title" : "중국",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/nx5k-SI0OP",
		"status" : 1
	},
	{
		"idx" : 2582,
		"title" : "김진목삼",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/HN1U16KgCI24",
		"status" : 1
	},
	{
		"idx" : 2583,
		"title" : "포항",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/97rg1lGNLdMm",
		"status" : 1
	},
	{
		"idx" : 2584,
		"title" : "뼈탄집",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/OVFm-4H6q8Zk",
		"status" : 1
	},
	{
		"idx" : 2585,
		"title" : "다차공간",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/jeDT7hYIGS5w",
		"status" : 1
	},
	{
		"idx" : 2586,
		"title" : "라멘시미즈",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/t6oxGDjInBYA",
		"status" : 1
	},
	{
		"idx" : 2587,
		"title" : "미트볼라운지",
		"score" : "4.4",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/od1sFzRjCXRi",
		"status" : 1
	},
	{
		"idx" : 2588,
		"title" : "칸다소바",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/5GKspyCnVLa0",
		"status" : 1
	},
	{
		"idx" : 2589,
		"title" : "포비",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/JlEOAtsbIt",
		"status" : 1
	},
	{
		"idx" : 2590,
		"title" : "이다",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/J3PdFUAW1z6v",
		"status" : 1
	},
	{
		"idx" : 2591,
		"title" : "핏제리아오",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/OhE_ArzacE",
		"status" : 1
	},
	{
		"idx" : 2592,
		"title" : "순희네빈대떡",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/Xpj5KZnWSt",
		"status" : 1
	},
	{
		"idx" : 2593,
		"title" : "황생가칼국수",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/mBD4XimUat",
		"status" : 1
	},
	{
		"idx" : 2594,
		"title" : "독도16도",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/QtVo0yPJLfgc",
		"status" : 1
	},
	{
		"idx" : 2595,
		"title" : "BAR CHAM",
		"score" : "4.8",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/lTMiXudtCvb4",
		"status" : 1
	},
	{
		"idx" : 2596,
		"title" : "데시데",
		"score" : "4.8",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/l0k43OGTH50J",
		"status" : 1
	},
	{
		"idx" : 2597,
		"title" : "우육면관",
		"score" : "4.8",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/cOPpYpvBoWrH",
		"status" : 1
	},
	{
		"idx" : 2598,
		"title" : "모던샤브하우스",
		"score" : "4.8",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/dzvLL3cnX1UC",
		"status" : 1
	},
	{
		"idx" : 2599,
		"title" : "효제루",
		"score" : "4.8",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/CxTm9IzfC5-x",
		"status" : 1
	},
	{
		"idx" : 2600,
		"title" : "만가타",
		"score" : "4.7",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/OJgUhmMaJOPI",
		"status" : 1
	},
	{
		"idx" : 2601,
		"title" : "호반",
		"score" : "4.7",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/-xVh_QZrOMo3",
		"status" : 1
	},
	{
		"idx" : 2602,
		"title" : "부촌육회",
		"score" : "4.7",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/mfpgS9_h0YYY",
		"status" : 1
	},
	{
		"idx" : 2603,
		"title" : "호라파",
		"score" : "4.7",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/6g1d24chargz",
		"status" : 1
	},
	{
		"idx" : 2604,
		"title" : "스시소라",
		"score" : "4.6",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/dlG6_fId6D2Y",
		"status" : 1
	},
	{
		"idx" : 2605,
		"title" : "팔마",
		"score" : "4.6",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/g-ZF2ky7D3m-",
		"status" : 1
	},
	{
		"idx" : 2606,
		"title" : "부촌육회",
		"score" : "4.6",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/AtNqVtENf9",
		"status" : 1
	},
	{
		"idx" : 2607,
		"title" : "우육면관",
		"score" : "4.6",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/3pC7ThiRL4MA",
		"status" : 1
	},
	{
		"idx" : 2608,
		"title" : "갈로팡",
		"score" : "4.6",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/28MrTng0ht8_",
		"status" : 1
	},
	{
		"idx" : 2609,
		"title" : "아키비스트",
		"score" : "4.6",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/IP_JKNwjYkyz",
		"status" : 1
	},
	{
		"idx" : 2610,
		"title" : "일월카츠",
		"score" : "4.6",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/GQPE6BUVsT-E",
		"status" : 1
	},
	{
		"idx" : 2611,
		"title" : "광장시장 찹쌀꽈배기",
		"score" : "4.6",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/g2Vx1VIr_pKo",
		"status" : 1
	},
	{
		"idx" : 2612,
		"title" : "밀림",
		"score" : "4.6",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/UITk5YXxI4Y8",
		"status" : 1
	},
	{
		"idx" : 2613,
		"title" : "고량주관",
		"score" : "4.6",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/BFTHhi0Ful3m",
		"status" : 1
	},
	{
		"idx" : 2614,
		"title" : "비엘티스테이크",
		"score" : "4.5",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/r5ZoupYsk_",
		"status" : 1
	},
	{
		"idx" : 2615,
		"title" : "대련집",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/a4Ux84gbMB",
		"status" : 1
	},
	{
		"idx" : 2616,
		"title" : "퀴진라끌레",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/_-j9nV0UhoNj",
		"status" : 1
	},
	{
		"idx" : 2617,
		"title" : "히타토제면소",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/CY_LGxIK9-s3",
		"status" : 1
	},
	{
		"idx" : 2618,
		"title" : "라쿠엔",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/3kNgXhlrkV_l",
		"status" : 1
	},
	{
		"idx" : 2619,
		"title" : "고트델리",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/mkxj-16Day5B",
		"status" : 1
	},
	{
		"idx" : 2620,
		"title" : "델리노쉬",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/_VDjdNyorAuy",
		"status" : 1
	},
	{
		"idx" : 2621,
		"title" : "오무사",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/PhhrfKOq1qSh",
		"status" : 1
	},
	{
		"idx" : 2622,
		"title" : "리본윈도우",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/9GTeBp6xtf",
		"status" : 1
	},
	{
		"idx" : 2623,
		"title" : "남대문막내횟집",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/t5nlPKpYGR",
		"status" : 1
	},
	{
		"idx" : 2624,
		"title" : "계향각",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/MbbMmTS5PU9c",
		"status" : 1
	},
	{
		"idx" : 2625,
		"title" : "은성횟집",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/Ui00v6pz_t",
		"status" : 1
	},
	{
		"idx" : 2626,
		"title" : "효도치킨",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/sBEJ0nlnODJI",
		"status" : 1
	},
	{
		"idx" : 2627,
		"title" : "고메오드",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/yOhmT3USJ6RR",
		"status" : 1
	},
	{
		"idx" : 2628,
		"title" : "동북화과왕",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/0MIHrLZjX8",
		"status" : 1
	},
	{
		"idx" : 2629,
		"title" : "청산손만두",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/7E-JOtMhuA",
		"status" : 1
	},
	{
		"idx" : 2630,
		"title" : "종로도담",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/5FxhKfdU-MqP",
		"status" : 1
	},
	{
		"idx" : 2631,
		"title" : "친니",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/iE3ng_QZDs",
		"status" : 1
	},
	{
		"idx" : 2632,
		"title" : "커피원",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/wfuQ9q2HTC6V",
		"status" : 1
	},
	{
		"idx" : 2633,
		"title" : "버터풀앤크리멀러스 쁘띠",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/NDc2WvFn5OfP",
		"status" : 1
	},
	{
		"idx" : 2634,
		"title" : "홍어랑민어랑",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/AiC8GfpxOBg-",
		"status" : 1
	},
	{
		"idx" : 2635,
		"title" : "아키라백",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/EQB1ieEn8jac",
		"status" : 1
	},
	{
		"idx" : 2636,
		"title" : "독일주택",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/rJ6av3SuzP",
		"status" : 1
	},
	{
		"idx" : 2637,
		"title" : "창신육회",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/0TkoIX33V9",
		"status" : 1
	},
	{
		"idx" : 2638,
		"title" : "평안도만두집",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/KxinsNEdHO",
		"status" : 1
	},
	{
		"idx" : 2639,
		"title" : "뚝배기집",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/RfROMZA_LS",
		"status" : 1
	},
	{
		"idx" : 2640,
		"title" : "키즈나",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/chr42BAu3pos",
		"status" : 1
	},
	{
		"idx" : 2641,
		"title" : "다운타우너",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/VvmJ6TnTs0av",
		"status" : 1
	},
	{
		"idx" : 2642,
		"title" : "통의동 국빈관",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/TntIkjwpCV40",
		"status" : 1
	},
	{
		"idx" : 2643,
		"title" : "화목순대국전문",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/myslZBeMRB",
		"status" : 1
	},
	{
		"idx" : 2644,
		"title" : "스쿠퍼",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/2z7g7MS7gbxx",
		"status" : 1
	},
	{
		"idx" : 2645,
		"title" : "어쩌다산책",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/6nFjiGvg-XaB",
		"status" : 1
	},
	{
		"idx" : 2646,
		"title" : "뎁짜이",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/f7uzonhiWb2d",
		"status" : 1
	},
	{
		"idx" : 2647,
		"title" : "반타이",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/8BR9vSdgpU",
		"status" : 1
	},
	{
		"idx" : 2648,
		"title" : "레이지버거클럽",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/6uX7yyYce_-1",
		"status" : 1
	},
	{
		"idx" : 2649,
		"title" : "이찌이스시",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/9vHLBTjW3m",
		"status" : 1
	},
	{
		"idx" : 2650,
		"title" : "차차 티클럽",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/DcLO81H570op",
		"status" : 1
	},
	{
		"idx" : 2651,
		"title" : "학술적연구소 (휴업중)",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/xVAE93pPwPHe",
		"status" : 1
	},
	{
		"idx" : 2652,
		"title" : "덕후선생",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/gTeEJOTziy1W",
		"status" : 1
	},
	{
		"idx" : 2653,
		"title" : "안덕",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/qcur99Rw1X3K",
		"status" : 1
	},
	{
		"idx" : 2654,
		"title" : "도트블랭킷",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/uFqIRgoPhzZt",
		"status" : 1
	},
	{
		"idx" : 2655,
		"title" : "밀과보리",
		"score" : "4.3",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/qjftqdHmQg0m",
		"status" : 1
	},
	{
		"idx" : 2656,
		"title" : "깡통만두",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/8lZn8Qcgj2",
		"status" : 1
	},
	{
		"idx" : 2657,
		"title" : "홈보이서울",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/Tk-FuSj-uebC",
		"status" : 1
	},
	{
		"idx" : 2658,
		"title" : "깔리",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/in8ezN7IbJ",
		"status" : 1
	},
	{
		"idx" : 2659,
		"title" : "서촌계단집",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/0FwTUkRDbF",
		"status" : 1
	},
	{
		"idx" : 2660,
		"title" : "Scoff",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/xYkBKtoLSJ",
		"status" : 1
	},
	{
		"idx" : 2661,
		"title" : "유유안",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/1euTBie3du",
		"status" : 1
	},
	{
		"idx" : 2662,
		"title" : "체부동잔치집",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/Ex276TuZzf",
		"status" : 1
	},
	{
		"idx" : 2663,
		"title" : "삼청동수제비",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/Jd6-L7seZK",
		"status" : 1
	},
	{
		"idx" : 2664,
		"title" : "기와탭룸",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/PP6LAC59_V",
		"status" : 1
	},
	{
		"idx" : 2665,
		"title" : "온천집",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/PF0lbeZG5Ak6",
		"status" : 1
	},
	{
		"idx" : 2666,
		"title" : "광화문뚝감",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/5w3XQVn5Ce",
		"status" : 1
	},
	{
		"idx" : 2667,
		"title" : "스시누하",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/gkyUZIJS4nB1",
		"status" : 1
	},
	{
		"idx" : 2668,
		"title" : "안암",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/eQEXwnrT4cpI",
		"status" : 1
	},
	{
		"idx" : 2669,
		"title" : "컨펙션스바이포시즌스",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/dYY1ICNl66",
		"status" : 1
	},
	{
		"idx" : 2670,
		"title" : "누룩나무",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/_sCP4T25rA",
		"status" : 1
	},
	{
		"idx" : 2671,
		"title" : "서울집시",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/qymOUBf1gHvU",
		"status" : 1
	},
	{
		"idx" : 2672,
		"title" : "애호락",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/kxHM5rmJo_t_",
		"status" : 1
	},
	{
		"idx" : 2673,
		"title" : "노브13",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/X7QWD3J8sEMS",
		"status" : 1
	},
	{
		"idx" : 2674,
		"title" : "혜화칼국수",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/GWwEwLw47W",
		"status" : 1
	},
	{
		"idx" : 2675,
		"title" : "알레그리아 덕수궁",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/Cc2LMGpjY-vv",
		"status" : 1
	},
	{
		"idx" : 2676,
		"title" : "그린냅",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/Kt7EGTNq1GcD",
		"status" : 1
	},
	{
		"idx" : 2677,
		"title" : "일번지",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/4PyqnM9bzufa",
		"status" : 1
	},
	{
		"idx" : 2678,
		"title" : "토리",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/sYleNQ7vmIrB",
		"status" : 1
	},
	{
		"idx" : 2679,
		"title" : "노말사이클코페",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/gpdIiD5W56Rj",
		"status" : 1
	},
	{
		"idx" : 2680,
		"title" : "전라도횟집",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/JDdP83HUyA",
		"status" : 1
	},
	{
		"idx" : 2681,
		"title" : "정돈",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/DsIDC233ow",
		"status" : 1
	},
	{
		"idx" : 2682,
		"title" : "오가와",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/ba-druB2Lm",
		"status" : 1
	},
	{
		"idx" : 2683,
		"title" : "고가빈커리하우스",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/Z7XW7OK7rLDi",
		"status" : 1
	},
	{
		"idx" : 2684,
		"title" : "힐사이드테이블",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/uaoz6fxCG-m8",
		"status" : 1
	},
	{
		"idx" : 2685,
		"title" : "멜팅샵X치즈룸",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/WOH1Di_ymm",
		"status" : 1
	},
	{
		"idx" : 2686,
		"title" : "갈리나데이지",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/HRA9FjXQ7Q",
		"status" : 1
	},
	{
		"idx" : 2687,
		"title" : "프릳츠커피컴퍼니",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/RACsFPJndwnv",
		"status" : 1
	},
	{
		"idx" : 2688,
		"title" : "룰스",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/U3s064HzJEyi",
		"status" : 1
	},
	{
		"idx" : 2689,
		"title" : "자하손만두",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/JP1_BO4rwf",
		"status" : 1
	},
	{
		"idx" : 2690,
		"title" : "에베레스트",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/QLglTnv05O",
		"status" : 1
	},
	{
		"idx" : 2691,
		"title" : "나무사이로",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/AdWddi4FyZ",
		"status" : 1
	},
	{
		"idx" : 2692,
		"title" : "리틀호호",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/IooT-KbZeD",
		"status" : 1
	},
	{
		"idx" : 2693,
		"title" : "나누미떡볶이",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/gKkMeMiEf7",
		"status" : 1
	},
	{
		"idx" : 2694,
		"title" : "사월의물고기",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/3z5dFcV_MaDG",
		"status" : 1
	},
	{
		"idx" : 2695,
		"title" : "서촌김씨뜨라또리아",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/-K8xNqMYg3e7",
		"status" : 1
	},
	{
		"idx" : 2696,
		"title" : "제이엘리",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/AtOStptqBKCl",
		"status" : 1
	},
	{
		"idx" : 2697,
		"title" : "애즈라이크",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/AWEt6DuE-jUl",
		"status" : 1
	},
	{
		"idx" : 2698,
		"title" : "드엠",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/UfIZP7OMkfW0",
		"status" : 1
	},
	{
		"idx" : 2699,
		"title" : "33마켓",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/oT9hmHBxTVwT",
		"status" : 1
	},
	{
		"idx" : 2700,
		"title" : "커피브론즈",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/G-er0UumQ4",
		"status" : 1
	},
	{
		"idx" : 2701,
		"title" : "오근내5닭갈비",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/p7RcdFzvS1w1",
		"status" : 1
	},
	{
		"idx" : 2702,
		"title" : "월하보이",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/XnskN1q3NQE4",
		"status" : 1
	},
	{
		"idx" : 2703,
		"title" : "자미더홍",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/IOc6QNkduV4v",
		"status" : 1
	},
	{
		"idx" : 2704,
		"title" : "스시쿠니",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/sEa4_ATH-AKx",
		"status" : 1
	},
	{
		"idx" : 2705,
		"title" : "서울상회",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/EZ9tRiTs1sq2",
		"status" : 1
	},
	{
		"idx" : 2706,
		"title" : "벅벅",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/kU488qF_pd-M",
		"status" : 1
	},
	{
		"idx" : 2707,
		"title" : "여기인가",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/0q1VeQ3JTQiT",
		"status" : 1
	},
	{
		"idx" : 2708,
		"title" : "이강순실비집",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/ScvFxttrdC",
		"status" : 1
	},
	{
		"idx" : 2709,
		"title" : "대하식당",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/IPufO3D23u",
		"status" : 1
	},
	{
		"idx" : 2710,
		"title" : "정담은보쌈",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/YrN13AoVurZQ",
		"status" : 1
	},
	{
		"idx" : 2711,
		"title" : "튀튀쿠키",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/5eM27kPex2wX",
		"status" : 1
	},
	{
		"idx" : 2712,
		"title" : "MERCAT",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/DUVVHj4lY79B",
		"status" : 1
	},
	{
		"idx" : 2713,
		"title" : "동묘집",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/9Q6umfJT4Dwz",
		"status" : 1
	},
	{
		"idx" : 2714,
		"title" : "부르크보드",
		"score" : "4.2",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/1c70vCBkIsp0",
		"status" : 1
	},
	{
		"idx" : 2715,
		"title" : "엄용백돼지국밥",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/5eeCIHrvdOec",
		"status" : 1
	},
	{
		"idx" : 2716,
		"title" : "서울서둘째로잘하는집",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/yHwF56gXZI",
		"status" : 1
	},
	{
		"idx" : 2717,
		"title" : "더피자필",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/zwpNx9vhflHr",
		"status" : 1
	},
	{
		"idx" : 2718,
		"title" : "뽐",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/x9wcU14GxkQA",
		"status" : 1
	},
	{
		"idx" : 2719,
		"title" : "카페 알베르게",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/gxK4Nu1-3nEd",
		"status" : 1
	},
	{
		"idx" : 2720,
		"title" : "코블러",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/OTGU4fKOV6K_",
		"status" : 1
	},
	{
		"idx" : 2721,
		"title" : "대성집",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/fSaeqC4xBF",
		"status" : 1
	},
	{
		"idx" : 2722,
		"title" : "홍성원",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/uGE6bDcbAR",
		"status" : 1
	},
	{
		"idx" : 2723,
		"title" : "비텔로소띠",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/uAsU8I-S2eA7",
		"status" : 1
	},
	{
		"idx" : 2724,
		"title" : "한옥달",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/SGqAjE0GRoR8",
		"status" : 1
	},
	{
		"idx" : 2725,
		"title" : "라뜰리에 꼼때",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/2pjUZsg1qq23",
		"status" : 1
	},
	{
		"idx" : 2726,
		"title" : "광화문더덕순대",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/Cwt-GIEYGQ5c",
		"status" : 1
	},
	{
		"idx" : 2727,
		"title" : "파틱",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/zOBaiXOgAOB2",
		"status" : 1
	},
	{
		"idx" : 2728,
		"title" : "마루",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/NcSajSFYm1",
		"status" : 1
	},
	{
		"idx" : 2729,
		"title" : "투뿔등심",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/b7oI38DCwD",
		"status" : 1
	},
	{
		"idx" : 2730,
		"title" : "법원",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/kyapbWR0pc5h",
		"status" : 1
	},
	{
		"idx" : 2731,
		"title" : "모루카츠",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/AhVTgas0nZlG",
		"status" : 1
	},
	{
		"idx" : 2732,
		"title" : "육회자매집",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/4eovy0JhPREm",
		"status" : 1
	},
	{
		"idx" : 2733,
		"title" : "명동닭한마리",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/w72lM5F0uz",
		"status" : 1
	},
	{
		"idx" : 2734,
		"title" : "경성양꼬치",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/oqsEPVUZy9",
		"status" : 1
	},
	{
		"idx" : 2735,
		"title" : "토속촌",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/EuYvGpXzeS",
		"status" : 1
	},
	{
		"idx" : 2736,
		"title" : "런던베이글뮤지엄",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/yDiTde5SjzuR",
		"status" : 1
	},
	{
		"idx" : 2737,
		"title" : "더마틴",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/gIiHRz8xuBur",
		"status" : 1
	},
	{
		"idx" : 2738,
		"title" : "청진옥",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/_plBHOtZL-",
		"status" : 1
	},
	{
		"idx" : 2739,
		"title" : "명륜건강원",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/CbWWt2r4FC4b",
		"status" : 1
	},
	{
		"idx" : 2740,
		"title" : "빚짜 이땔리방앗간",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/P3KBWcI6O8",
		"status" : 1
	},
	{
		"idx" : 2741,
		"title" : "유진식당",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/5bGfYaBNoX",
		"status" : 1
	},
	{
		"idx" : 2742,
		"title" : "비엣꽌",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/QITJKiSkQM",
		"status" : 1
	},
	{
		"idx" : 2743,
		"title" : "모도우",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/h85z0axKmywu",
		"status" : 1
	},
	{
		"idx" : 2744,
		"title" : "내자상회",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/CVVJw_-7zG9b",
		"status" : 1
	},
	{
		"idx" : 2745,
		"title" : "안주마을",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/-x6kObCaJ0",
		"status" : 1
	},
	{
		"idx" : 2746,
		"title" : "인왕산대충유원지",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/g05ayUaWyfCe",
		"status" : 1
	},
	{
		"idx" : 2747,
		"title" : "두오모",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/lEBnB3k3ss",
		"status" : 1
	},
	{
		"idx" : 2748,
		"title" : "마이클 바이 해비치",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/s44Blc4tkKkn",
		"status" : 1
	},
	{
		"idx" : 2749,
		"title" : "비스트로친친",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/jLzQ0b1Uyy",
		"status" : 1
	},
	{
		"idx" : 2750,
		"title" : "어바웃진스",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/jOuvoEF7AlnM",
		"status" : 1
	},
	{
		"idx" : 2751,
		"title" : "국수찾아닭만리",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/vFcy-zyXpmc4",
		"status" : 1
	},
	{
		"idx" : 2752,
		"title" : "오수흑두부",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/jn8UL9KzLY",
		"status" : 1
	},
	{
		"idx" : 2753,
		"title" : "암소서울",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/vmfCUuCAm-HV",
		"status" : 1
	},
	{
		"idx" : 2754,
		"title" : "칸다소바",
		"score" : "4.1",
		"region" : "종로구",
		"url" : "https://www.mangoplate.com/restaurants/uUfiTeQAUX7q",
		"status" : 1
	},
	{
		"idx" : 2755,
		"title" : "어머니대성집",
		"score" : "4.5",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/9Gi6030AUV",
		"status" : 1
	},
	{
		"idx" : 2756,
		"title" : "시키카츠",
		"score" : "4.5",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/LtQEW4w1BZMm",
		"status" : 1
	},
	{
		"idx" : 2757,
		"title" : "만감",
		"score" : "4.5",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/EB4ppf5Ku0hd",
		"status" : 1
	},
	{
		"idx" : 2758,
		"title" : "육전식당",
		"score" : "4.4",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/qiinV6W6sC",
		"status" : 1
	},
	{
		"idx" : 2759,
		"title" : "나정순할매쭈꾸미",
		"score" : "4.4",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/_3QOogUbde",
		"status" : 1
	},
	{
		"idx" : 2760,
		"title" : "래디컬브루잉클럽",
		"score" : "4.4",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/c1QL0CJNEsCo",
		"status" : 1
	},
	{
		"idx" : 2761,
		"title" : "홍릉각",
		"score" : "4.3",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/CIWgIL2M1R",
		"status" : 1
	},
	{
		"idx" : 2762,
		"title" : "영천선비",
		"score" : "4.3",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/7U4CdZt0LWLc",
		"status" : 1
	},
	{
		"idx" : 2763,
		"title" : "안동집손칼국시",
		"score" : "4.3",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/Y0B2KNSMHj",
		"status" : 1
	},
	{
		"idx" : 2764,
		"title" : "콘반",
		"score" : "4.3",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/7f4KWFnrPAzm",
		"status" : 1
	},
	{
		"idx" : 2765,
		"title" : "비나",
		"score" : "4.3",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/7ngJn9NG-P",
		"status" : 1
	},
	{
		"idx" : 2766,
		"title" : "도톰",
		"score" : "4.3",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/wuXrWbNyOiLC",
		"status" : 1
	},
	{
		"idx" : 2767,
		"title" : "정편백",
		"score" : "4.3",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/rNAyUMMzjrn8",
		"status" : 1
	},
	{
		"idx" : 2768,
		"title" : "남원통닭",
		"score" : "4.3",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/djHjmvdHf2eg",
		"status" : 1
	},
	{
		"idx" : 2769,
		"title" : "스시코야",
		"score" : "4.2",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/V-MJpnrhfYyO",
		"status" : 1
	},
	{
		"idx" : 2770,
		"title" : "성천막국수",
		"score" : "4.2",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/SJ7rdMU9Tm",
		"status" : 1
	},
	{
		"idx" : 2771,
		"title" : "돈부각",
		"score" : "4.2",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/M5i9v-ZrmhWH",
		"status" : 1
	},
	{
		"idx" : 2772,
		"title" : "커피그라운즈",
		"score" : "4.2",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/8DYOBS7idi5f",
		"status" : 1
	},
	{
		"idx" : 2773,
		"title" : "골목길빵공작소",
		"score" : "4.2",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/SYl8ehS0tR_1",
		"status" : 1
	},
	{
		"idx" : 2774,
		"title" : "촨커",
		"score" : "4.2",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/WkEZfRVlERNa",
		"status" : 1
	},
	{
		"idx" : 2775,
		"title" : "서울뼈구이매운족발",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/PbXcoP50d4D9",
		"status" : 1
	},
	{
		"idx" : 2776,
		"title" : "경발원",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/0QGJwfVJB6",
		"status" : 1
	},
	{
		"idx" : 2777,
		"title" : "레알라면",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/lTG5yMCmrK",
		"status" : 1
	},
	{
		"idx" : 2778,
		"title" : "팔레트",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/Mj9XJsraWwNp",
		"status" : 1
	},
	{
		"idx" : 2779,
		"title" : "일미식당",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/0sZSd5kPfHEi",
		"status" : 1
	},
	{
		"idx" : 2780,
		"title" : "고깃집도훈",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/-4OAkN6gS-Ao",
		"status" : 1
	},
	{
		"idx" : 2781,
		"title" : "사골마라탕",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/USulz-1hjYCr",
		"status" : 1
	},
	{
		"idx" : 2782,
		"title" : "수퍼보울",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/6w5aSMFRrLcR",
		"status" : 1
	},
	{
		"idx" : 2783,
		"title" : "언니네함바그",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/HKyPtqgsjxlY",
		"status" : 1
	},
	{
		"idx" : 2784,
		"title" : "컴플리트커피",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/D2P-Zl8YrTJr",
		"status" : 1
	},
	{
		"idx" : 2785,
		"title" : "신락원",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/dHqsH6TbFO4A",
		"status" : 1
	},
	{
		"idx" : 2786,
		"title" : "슈퍼내추럴",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/9C23mq8B5aio",
		"status" : 1
	},
	{
		"idx" : 2787,
		"title" : "스시선생",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/2kJRDrbCRsb_",
		"status" : 1
	},
	{
		"idx" : 2788,
		"title" : "봉이만두",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/dtzG9pA5d4",
		"status" : 1
	},
	{
		"idx" : 2789,
		"title" : "Coffee Methodz",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/UDx6zEriFXoD",
		"status" : 1
	},
	{
		"idx" : 2790,
		"title" : "꼬로노이",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/LvxCAHazmdrW",
		"status" : 1
	},
	{
		"idx" : 2791,
		"title" : "스시고이",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/Az-LHu9E1oWf",
		"status" : 1
	},
	{
		"idx" : 2792,
		"title" : "장군집",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/o62mCHXAO9",
		"status" : 1
	},
	{
		"idx" : 2793,
		"title" : "할머니냉면집",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/vgHApUPPfR",
		"status" : 1
	},
	{
		"idx" : 2794,
		"title" : "감초식당",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/FIMCuT75DrLJ",
		"status" : 1
	},
	{
		"idx" : 2795,
		"title" : "본가할머니보쌈",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/TOYufi-U41",
		"status" : 1
	},
	{
		"idx" : 2796,
		"title" : "망우로30",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/PqeWb4LBdSJ9",
		"status" : 1
	},
	{
		"idx" : 2797,
		"title" : "키라쿠",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/kQgtHtgEyem9",
		"status" : 1
	},
	{
		"idx" : 2798,
		"title" : "메이크샐러드",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/76Kcri3VImx6",
		"status" : 1
	},
	{
		"idx" : 2799,
		"title" : "칠기마라탕",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/ssqt-hT_P11v",
		"status" : 1
	},
	{
		"idx" : 2800,
		"title" : "와요",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/_x4ItK77h_AA",
		"status" : 1
	},
	{
		"idx" : 2801,
		"title" : "오소록",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/IN73SoVvbyuO",
		"status" : 1
	},
	{
		"idx" : 2802,
		"title" : "거복이식당",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/aMt_9zjFvvow",
		"status" : 1
	},
	{
		"idx" : 2803,
		"title" : "푸른하늘",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/BeWD1yD3FINi",
		"status" : 1
	},
	{
		"idx" : 2804,
		"title" : "메모아르",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/w7oB05gEgszE",
		"status" : 1
	},
	{
		"idx" : 2805,
		"title" : "코코니주방",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/_iQtia04BnMJ",
		"status" : 1
	},
	{
		"idx" : 2806,
		"title" : "키친요로시쿠",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/DfOV4xWrrJ_4",
		"status" : 1
	},
	{
		"idx" : 2807,
		"title" : "Mods Place",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/V_aS9YO6guCc",
		"status" : 1
	},
	{
		"idx" : 2808,
		"title" : "카페양귀비",
		"score" : "3.6",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/IiaW0txvzPES",
		"status" : 1
	},
	{
		"idx" : 2809,
		"title" : "이모네파전",
		"score" : "3.6",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/OQK_bh6VDJ",
		"status" : 1
	},
	{
		"idx" : 2810,
		"title" : "컴투레스트",
		"score" : "3.6",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/fOOuOq5bscwV",
		"status" : 1
	},
	{
		"idx" : 2811,
		"title" : "카페 대즐링",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/870aQkwSvNCE",
		"status" : 1
	},
	{
		"idx" : 2812,
		"title" : "은하곱창",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/Ag17F8c_LU",
		"status" : 1
	},
	{
		"idx" : 2813,
		"title" : "놀부만두",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/9hue2ED01T",
		"status" : 1
	},
	{
		"idx" : 2814,
		"title" : "치맥파이브",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/VIHdM1qYGm",
		"status" : 1
	},
	{
		"idx" : 2815,
		"title" : "알로하올라",
		"score" : "4.2",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/SOsK54wpS2Ks",
		"status" : 1
	},
	{
		"idx" : 2816,
		"title" : "회기왕족발보쌈",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/A1fJgDwgys",
		"status" : 1
	},
	{
		"idx" : 2817,
		"title" : "영화장",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/mobf5W8DZ-",
		"status" : 1
	},
	{
		"idx" : 2818,
		"title" : "King수제만두",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/LIakXRkYhiQ2",
		"status" : 1
	},
	{
		"idx" : 2819,
		"title" : "육전식당",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/hQcXtV8-2elp",
		"status" : 1
	},
	{
		"idx" : 2820,
		"title" : "이문동커피집",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/FOa9F1Mb6Z4r",
		"status" : 1
	},
	{
		"idx" : 2821,
		"title" : "답십리별미",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/frrNyrzvzsm1",
		"status" : 1
	},
	{
		"idx" : 2822,
		"title" : "와가리피순대",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/4gd44t-YMV",
		"status" : 1
	},
	{
		"idx" : 2823,
		"title" : "춘천메밀막국수",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/W3VwmcveCT6J",
		"status" : 1
	},
	{
		"idx" : 2824,
		"title" : "대흥설농탕",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/m3ouoMjqwVmg",
		"status" : 1
	},
	{
		"idx" : 2825,
		"title" : "멍군집",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/Mr0wKNf8w2E-",
		"status" : 1
	},
	{
		"idx" : 2826,
		"title" : "연어이야기",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/1AX_fB5bZ3Gc",
		"status" : 1
	},
	{
		"idx" : 2827,
		"title" : "포레스티",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/yQFcfSnAtY",
		"status" : 1
	},
	{
		"idx" : 2828,
		"title" : "토성옥",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/0mmP1VPR5g6E",
		"status" : 1
	},
	{
		"idx" : 2829,
		"title" : "에잇올리",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/forwUl9H9VBr",
		"status" : 1
	},
	{
		"idx" : 2830,
		"title" : "고래돈가스",
		"score" : "4.1",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/fwR_SKwmnk",
		"status" : 1
	},
	{
		"idx" : 2831,
		"title" : "오관스시",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/eMt3D3VCFOvi",
		"status" : 1
	},
	{
		"idx" : 2832,
		"title" : "혜성칼국수",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/vGVdeXSlJ0",
		"status" : 1
	},
	{
		"idx" : 2833,
		"title" : "79번지국수집",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/68N07P0DUC",
		"status" : 1
	},
	{
		"idx" : 2834,
		"title" : "홍콩중화요리",
		"score" : "4.0",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/B-AdCzkEOOnS",
		"status" : 1
	},
	{
		"idx" : 2835,
		"title" : "돼랑이우랑이",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/M5Jb8LvI_5hp",
		"status" : 1
	},
	{
		"idx" : 2836,
		"title" : "군만두의달인",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/_dKkU2_3zz9A",
		"status" : 1
	},
	{
		"idx" : 2837,
		"title" : "이상한떡볶이집",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/WYsSbcdvXE",
		"status" : 1
	},
	{
		"idx" : 2838,
		"title" : "아임파이",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/BCLr2j1YYePJ",
		"status" : 1
	},
	{
		"idx" : 2839,
		"title" : "커피디엔에이로스팅컴퍼니",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/XzJN6t2zOr",
		"status" : 1
	},
	{
		"idx" : 2840,
		"title" : "헤이피",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/ZZyjKfn7TFOG",
		"status" : 1
	},
	{
		"idx" : 2841,
		"title" : "인더베이글",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/uok-JMlRl1DL",
		"status" : 1
	},
	{
		"idx" : 2842,
		"title" : "배트콩",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/3G5jNNu9-7",
		"status" : 1
	},
	{
		"idx" : 2843,
		"title" : "라구퀸",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/_l--Ccsnvw7a",
		"status" : 1
	},
	{
		"idx" : 2844,
		"title" : "특별식당",
		"score" : "3.9",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/LJUTTVFJIzS-",
		"status" : 1
	},
	{
		"idx" : 2845,
		"title" : "물고기",
		"score" : "3.8",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/EFihbBJkmhGq",
		"status" : 1
	},
	{
		"idx" : 2846,
		"title" : "백수씨심야식당",
		"score" : "3.8",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/7BQ_9brEmB",
		"status" : 1
	},
	{
		"idx" : 2847,
		"title" : "치보",
		"score" : "3.8",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/WUDGGzGwrK",
		"status" : 1
	},
	{
		"idx" : 2848,
		"title" : "여기가좋겠네",
		"score" : "3.8",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/RONlqIZ1cE",
		"status" : 1
	},
	{
		"idx" : 2849,
		"title" : "고향집",
		"score" : "3.8",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/WdeqbF7RtvlX",
		"status" : 1
	},
	{
		"idx" : 2850,
		"title" : "미뇽",
		"score" : "3.8",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/1hW1NcB6W0Mj",
		"status" : 1
	},
	{
		"idx" : 2851,
		"title" : "카페파인",
		"score" : "3.8",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/cY_QvP8XwkW-",
		"status" : 1
	},
	{
		"idx" : 2852,
		"title" : "회기버거",
		"score" : "3.8",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/DWtrrQs8tdzs",
		"status" : 1
	},
	{
		"idx" : 2853,
		"title" : "히노하루",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/xQg7xKulaG",
		"status" : 1
	},
	{
		"idx" : 2854,
		"title" : "평양냉면",
		"score" : "3.7",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/csTCijDcVo",
		"status" : 1
	},
	{
		"idx" : 2855,
		"title" : "고기야미안해",
		"score" : "3.6",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/lco-ulKKn8",
		"status" : 1
	},
	{
		"idx" : 2856,
		"title" : "일미간장게장",
		"score" : "3.6",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/gwRdfp4keo",
		"status" : 1
	},
	{
		"idx" : 2857,
		"title" : "마루기",
		"score" : "3.6",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/FOMRC5r3iK",
		"status" : 1
	},
	{
		"idx" : 2858,
		"title" : "미연양꼬치",
		"score" : "3.6",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/ATLZU2H32mTQ",
		"status" : 1
	},
	{
		"idx" : 2859,
		"title" : "커피나인",
		"score" : "3.6",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/7PNVOYXQct",
		"status" : 1
	},
	{
		"idx" : 2860,
		"title" : "카페브레송",
		"score" : "3.6",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/c_70oGYRAP",
		"status" : 1
	},
	{
		"idx" : 2861,
		"title" : "비하인드미",
		"score" : "3.5",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/aVu19Pnb77BM",
		"status" : 1
	},
	{
		"idx" : 2862,
		"title" : "장안정",
		"score" : "3.5",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/n5JCknIO9b",
		"status" : 1
	},
	{
		"idx" : 2863,
		"title" : "고황24시 뼈다귀해장국감자탕",
		"score" : "3.5",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/Ln6nQQH5NU",
		"status" : 1
	},
	{
		"idx" : 2864,
		"title" : "8 Street",
		"score" : "3.5",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/qYSRDXiWr9",
		"status" : 1
	},
	{
		"idx" : 2865,
		"title" : "식닷컴",
		"score" : "3.5",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/ymu_wGfufZz9",
		"status" : 1
	},
	{
		"idx" : 2866,
		"title" : "동경통닭",
		"score" : "3.5",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/uPIRY77yD3vq",
		"status" : 1
	},
	{
		"idx" : 2867,
		"title" : "광주식당",
		"score" : "3.5",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/3Z-noiSPcB",
		"status" : 1
	},
	{
		"idx" : 2868,
		"title" : "39돈가스",
		"score" : "3.5",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/iaTuXa5Xa1yW",
		"status" : 1
	},
	{
		"idx" : 2869,
		"title" : "홍곱창",
		"score" : "3.4",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/Dl93Wo3-mF",
		"status" : 1
	},
	{
		"idx" : 2870,
		"title" : "고소운",
		"score" : "3.4",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/9RQBq4okfR6J",
		"status" : 1
	},
	{
		"idx" : 2871,
		"title" : "코지인무르무르",
		"score" : "3.4",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/K0_6IRVo3Mp6",
		"status" : 1
	},
	{
		"idx" : 2872,
		"title" : "크로네",
		"score" : "3.4",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/5wsJohzNPn",
		"status" : 1
	},
	{
		"idx" : 2873,
		"title" : "일곱평",
		"score" : "3.4",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/ylma-g1XuTiA",
		"status" : 1
	},
	{
		"idx" : 2874,
		"title" : "돈부리청년",
		"score" : "3.4",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/-v5SBfECMg",
		"status" : 1
	},
	{
		"idx" : 2875,
		"title" : "독",
		"score" : "3.4",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/epQUls63eU",
		"status" : 1
	},
	{
		"idx" : 2876,
		"title" : "시카고커리",
		"score" : "3.4",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/a-MGBy3nEDC8",
		"status" : 1
	},
	{
		"idx" : 2877,
		"title" : "스타벅스",
		"score" : "3.3",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/SC56EHiEiXDK",
		"status" : 1
	},
	{
		"idx" : 2878,
		"title" : "마카나이",
		"score" : "3.3",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/IjWsdy8jyI",
		"status" : 1
	},
	{
		"idx" : 2879,
		"title" : "도란도란야채곱창",
		"score" : "3.2",
		"region" : "동대문구",
		"url" : "https://www.mangoplate.com/restaurants/TY8Uq1qTWl",
		"status" : 1
	},
	{
		"idx" : 2880,
		"title" : "용마해장국",
		"score" : "4.3",
		"region" : "중랑구",
		"url" : "https://www.mangoplate.com/restaurants/YkdHLFhFBIil",
		"status" : 1
	},
	{
		"idx" : 2881,
		"title" : "티하우스나니",
		"score" : "4.2",
		"region" : "중랑구",
		"url" : "https://www.mangoplate.com/restaurants/GyU7eEsjUSSh",
		"status" : 1
	},
	{
		"idx" : 2882,
		"title" : "만두만",
		"score" : "4.2",
		"region" : "중랑구",
		"url" : "https://www.mangoplate.com/restaurants/yKXfFvUaPYw5",
		"status" : 1
	},
	{
		"idx" : 2883,
		"title" : "팡도리노",
		"score" : "3.9",
		"region" : "중랑구",
		"url" : "https://www.mangoplate.com/restaurants/RoQntOyDh19Y",
		"status" : 1
	},
	{
		"idx" : 2884,
		"title" : "면동떡볶이",
		"score" : "3.9",
		"region" : "중랑구",
		"url" : "https://www.mangoplate.com/restaurants/ogYbqWHby8a6",
		"status" : 1
	},
	{
		"idx" : 2885,
		"title" : "찜집",
		"score" : "3.8",
		"region" : "중랑구",
		"url" : "https://www.mangoplate.com/restaurants/suxgGTkFc-AA",
		"status" : 1
	},
	{
		"idx" : 2886,
		"title" : "한참치",
		"score" : "3.7",
		"region" : "중랑구",
		"url" : "https://www.mangoplate.com/restaurants/ToEBOcoZdf",
		"status" : 1
	},
	{
		"idx" : 2887,
		"title" : "함평국밥",
		"score" : "3.7",
		"region" : "중랑구",
		"url" : "https://www.mangoplate.com/restaurants/3Ou_L16vKuhE",
		"status" : 1
	},
	{
		"idx" : 2888,
		"title" : "스시고메이",
		"score" : "3.6",
		"region" : "중랑구",
		"url" : "https://www.mangoplate.com/restaurants/mYfgdCWGzb",
		"status" : 1
	},
	{
		"idx" : 2889,
		"title" : "홍이네떡볶이",
		"score" : "3.6",
		"region" : "중랑구",
		"url" : "https://www.mangoplate.com/restaurants/aW7c-jUFeu",
		"status" : 1
	},
	{
		"idx" : 2890,
		"title" : "태능배밭갈비",
		"score" : "3.5",
		"region" : "중랑구",
		"url" : "https://www.mangoplate.com/restaurants/BV6wfViPpa",
		"status" : 1
	},
	{
		"idx" : 2891,
		"title" : "어글리스토브",
		"score" : "3.1",
		"region" : "중랑구",
		"url" : "https://www.mangoplate.com/restaurants/0FIbwSkOq8wY",
		"status" : 1
	},
	{
		"idx" : 2892,
		"title" : "천막집",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/FRz3_-PQrWMI",
		"status" : 1
	},
	{
		"idx" : 2893,
		"title" : "모짜",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/L9uOdmF_mKMs",
		"status" : 1
	},
	{
		"idx" : 2894,
		"title" : "버거파크",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/JgMnltOeKgWl",
		"status" : 1
	},
	{
		"idx" : 2895,
		"title" : "성북동면옥집",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/aeFW8M-SxE66",
		"status" : 1
	},
	{
		"idx" : 2896,
		"title" : "국시집",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/D2kHGNqO-H",
		"status" : 1
	},
	{
		"idx" : 2897,
		"title" : "제뉴어리피크닉",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/_IFjYhOeHo7D",
		"status" : 1
	},
	{
		"idx" : 2898,
		"title" : "일상",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/7NSTKgnqPh",
		"status" : 1
	},
	{
		"idx" : 2899,
		"title" : "수아당",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/JPiGO7Fv4PI7",
		"status" : 1
	},
	{
		"idx" : 2900,
		"title" : "봉화묵집",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/XA7_zOznCn",
		"status" : 1
	},
	{
		"idx" : 2901,
		"title" : "계모임",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Iz2fZDfNZoS6",
		"status" : 1
	},
	{
		"idx" : 2902,
		"title" : "할매숯불닭갈비",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/g1BLFzjtla",
		"status" : 1
	},
	{
		"idx" : 2903,
		"title" : "한상차림밥상",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/EgDENGavulNb",
		"status" : 1
	},
	{
		"idx" : 2904,
		"title" : "어흥식당",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/gavMtZa2O4hU",
		"status" : 1
	},
	{
		"idx" : 2905,
		"title" : "이공김밥",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/PQpshHG-Qsj4",
		"status" : 1
	},
	{
		"idx" : 2906,
		"title" : "퍽앤어니언",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/-VjQkk_felhx",
		"status" : 1
	},
	{
		"idx" : 2907,
		"title" : "샌드위치하우스",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/bfq8DiSUHN",
		"status" : 1
	},
	{
		"idx" : 2908,
		"title" : "오버스토리",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/1dzO6FrAqIZS",
		"status" : 1
	},
	{
		"idx" : 2909,
		"title" : "바스크",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/ktr3bNQbAUYj",
		"status" : 1
	},
	{
		"idx" : 2910,
		"title" : "선동보리밥",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/2YSCs_w5pN",
		"status" : 1
	},
	{
		"idx" : 2911,
		"title" : "모던양갱집",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/5c63KN0nfa-3",
		"status" : 1
	},
	{
		"idx" : 2912,
		"title" : "성북동집",
		"score" : "4.2",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/6Sak50haNw",
		"status" : 1
	},
	{
		"idx" : 2913,
		"title" : "바람난오리궁뎅이",
		"score" : "4.2",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/ZQdtYA4_XP",
		"status" : 1
	},
	{
		"idx" : 2914,
		"title" : "동우설렁탕",
		"score" : "4.2",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/zYDl6T42K3",
		"status" : 1
	},
	{
		"idx" : 2915,
		"title" : "반지",
		"score" : "4.2",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/upV_t2JCa9uV",
		"status" : 1
	},
	{
		"idx" : 2916,
		"title" : "성북동누룽지백숙",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/umsnSFGjPn",
		"status" : 1
	},
	{
		"idx" : 2917,
		"title" : "동병상련",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/FEPbvDw4Co",
		"status" : 1
	},
	{
		"idx" : 2918,
		"title" : "팔백집",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/59XPhjKN3In9",
		"status" : 1
	},
	{
		"idx" : 2919,
		"title" : "오샬",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/L1APObdFNg",
		"status" : 1
	},
	{
		"idx" : 2920,
		"title" : "영순관",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/myF2n0czDs5N",
		"status" : 1
	},
	{
		"idx" : 2921,
		"title" : "스프레드",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/3T29esws69iY",
		"status" : 1
	},
	{
		"idx" : 2922,
		"title" : "샤뽀블랑",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/z4QOdNn74G",
		"status" : 1
	},
	{
		"idx" : 2923,
		"title" : "구포국수",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/exHglANmLO",
		"status" : 1
	},
	{
		"idx" : 2924,
		"title" : "제주고깃집",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/mUC5q2BOGJ4t",
		"status" : 1
	},
	{
		"idx" : 2925,
		"title" : "달콤한위로",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/tCSWPU0_iWWv",
		"status" : 1
	},
	{
		"idx" : 2926,
		"title" : "비나케이크",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/QQYLNYrvxm",
		"status" : 1
	},
	{
		"idx" : 2927,
		"title" : "길음모소리",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/j6eZnp_ZFvCB",
		"status" : 1
	},
	{
		"idx" : 2928,
		"title" : "동선식당",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/223X9vmG72ET",
		"status" : 1
	},
	{
		"idx" : 2929,
		"title" : "와플앨리",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/VgZDyqW0hd",
		"status" : 1
	},
	{
		"idx" : 2930,
		"title" : "호랑이김밥",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/pXFbgqVbIx-3",
		"status" : 1
	},
	{
		"idx" : 2931,
		"title" : "일미옥",
		"score" : "4.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/vaO8Ko_TPa",
		"status" : 1
	},
	{
		"idx" : 2932,
		"title" : "밀곳간",
		"score" : "4.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/6egenVr-V_6-",
		"status" : 1
	},
	{
		"idx" : 2933,
		"title" : "카레",
		"score" : "4.6",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/jJVFxakTvMh_",
		"status" : 1
	},
	{
		"idx" : 2934,
		"title" : "도이칠란드 박",
		"score" : "4.6",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/p4hlQ7fhOfyO",
		"status" : 1
	},
	{
		"idx" : 2935,
		"title" : "공푸",
		"score" : "4.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/gZgArT4cSW",
		"status" : 1
	},
	{
		"idx" : 2936,
		"title" : "뽀르께노 스페니쉬비스트로",
		"score" : "4.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/EvC4Q5VZ0B1x",
		"status" : 1
	},
	{
		"idx" : 2937,
		"title" : "드시소",
		"score" : "4.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/X2ur1QhYfnDk",
		"status" : 1
	},
	{
		"idx" : 2938,
		"title" : "토로생선구이",
		"score" : "4.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/j4sCtlSB4z2A",
		"status" : 1
	},
	{
		"idx" : 2939,
		"title" : "쎄오쎄오",
		"score" : "4.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Smyv9xGs7-1J",
		"status" : 1
	},
	{
		"idx" : 2940,
		"title" : "우정초밥",
		"score" : "4.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/jFWl95c1KbXZ",
		"status" : 1
	},
	{
		"idx" : 2941,
		"title" : "고른햇살",
		"score" : "4.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/c2Y7nyFdix",
		"status" : 1
	},
	{
		"idx" : 2942,
		"title" : "스시다온",
		"score" : "4.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/1uma03xF5wFB",
		"status" : 1
	},
	{
		"idx" : 2943,
		"title" : "안동반점",
		"score" : "4.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/R8vsQqAAiA",
		"status" : 1
	},
	{
		"idx" : 2944,
		"title" : "치티",
		"score" : "4.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/TSutCVCcprYS",
		"status" : 1
	},
	{
		"idx" : 2945,
		"title" : "임금님자장면",
		"score" : "4.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/fVurDznkSk",
		"status" : 1
	},
	{
		"idx" : 2946,
		"title" : "유목커피바",
		"score" : "4.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/reQjs6VQE8Fo",
		"status" : 1
	},
	{
		"idx" : 2947,
		"title" : "참나무닭나라",
		"score" : "4.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/CWYsl16IPZ",
		"status" : 1
	},
	{
		"idx" : 2948,
		"title" : "일흥콩나물국밥",
		"score" : "4.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/37XDov1cWC",
		"status" : 1
	},
	{
		"idx" : 2949,
		"title" : "추랑",
		"score" : "4.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/vZT91UTqcmpk",
		"status" : 1
	},
	{
		"idx" : 2950,
		"title" : "옥돌",
		"score" : "4.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/tmWQLjCoiqIF",
		"status" : 1
	},
	{
		"idx" : 2951,
		"title" : "애정마라샹궈",
		"score" : "4.2",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/4k8p-1IcCal0",
		"status" : 1
	},
	{
		"idx" : 2952,
		"title" : "선화슈퍼",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/2tYZ3uruV4Wt",
		"status" : 1
	},
	{
		"idx" : 2953,
		"title" : "미스터국밥",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/nRobGmfUhhsE",
		"status" : 1
	},
	{
		"idx" : 2954,
		"title" : "이상조전통만두국",
		"score" : "4.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Db15GaxU92",
		"status" : 1
	},
	{
		"idx" : 2955,
		"title" : "네임드에스프레소",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Eamjd7fXdWEO",
		"status" : 1
	},
	{
		"idx" : 2956,
		"title" : "디어브레드",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/n3yDXbvBOw",
		"status" : 1
	},
	{
		"idx" : 2957,
		"title" : "라라면가",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/xC9tTeBtAhTs",
		"status" : 1
	},
	{
		"idx" : 2958,
		"title" : "너의냠냠버거",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/2TOOvoicTK8d",
		"status" : 1
	},
	{
		"idx" : 2959,
		"title" : "용초수",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/uXnu4SU_Bg",
		"status" : 1
	},
	{
		"idx" : 2960,
		"title" : "카페그레도",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/0Vh1_fUURlo8",
		"status" : 1
	},
	{
		"idx" : 2961,
		"title" : "청수장",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Occ-0Eb_J5",
		"status" : 1
	},
	{
		"idx" : 2962,
		"title" : "샐러드프린세스",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/RQLNHzqpIb",
		"status" : 1
	},
	{
		"idx" : 2963,
		"title" : "야마토텐동",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/b10yM0gg8AP-",
		"status" : 1
	},
	{
		"idx" : 2964,
		"title" : "히포크라테스 스프",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/egt9mSPezlCz",
		"status" : 1
	},
	{
		"idx" : 2965,
		"title" : "김통",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/lwy8t69r2KrH",
		"status" : 1
	},
	{
		"idx" : 2966,
		"title" : "보편적연어",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/owKINyfK3yZ3",
		"status" : 1
	},
	{
		"idx" : 2967,
		"title" : "안선생주가",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/C47WDKQcSk3H",
		"status" : 1
	},
	{
		"idx" : 2968,
		"title" : "모블러",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/d7omveQ90s37",
		"status" : 1
	},
	{
		"idx" : 2969,
		"title" : "리이케",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/o7FwL-166-Ww",
		"status" : 1
	},
	{
		"idx" : 2970,
		"title" : "우주제빵소",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/GEov6J3B-h_l",
		"status" : 1
	},
	{
		"idx" : 2971,
		"title" : "명문막국수",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/tONq0qyfKG",
		"status" : 1
	},
	{
		"idx" : 2972,
		"title" : "백두산양꼬치구이",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/ArYOz3UOMR",
		"status" : 1
	},
	{
		"idx" : 2973,
		"title" : "카페58.4",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/NBqRm4DJDFfX",
		"status" : 1
	},
	{
		"idx" : 2974,
		"title" : "루틴",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/eTvAY1e6Blvw",
		"status" : 1
	},
	{
		"idx" : 2975,
		"title" : "니르코브",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/8AfPrmT_DtpS",
		"status" : 1
	},
	{
		"idx" : 2976,
		"title" : "우리할매떡볶이",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/D5Y5XK2q3IEQ",
		"status" : 1
	},
	{
		"idx" : 2977,
		"title" : "핸썸베이글",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/4jN4ZbkJiA",
		"status" : 1
	},
	{
		"idx" : 2978,
		"title" : "카페애일",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/whncy7umU5tt",
		"status" : 1
	},
	{
		"idx" : 2979,
		"title" : "춘자",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/2kmbcF4Ag4",
		"status" : 1
	},
	{
		"idx" : 2980,
		"title" : "이세돈가스",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/7B_0YP4PXY3L",
		"status" : 1
	},
	{
		"idx" : 2981,
		"title" : "기차순대국",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Twy8BJojdH",
		"status" : 1
	},
	{
		"idx" : 2982,
		"title" : "땡스롤리",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/aQe6lB4xhm9W",
		"status" : 1
	},
	{
		"idx" : 2983,
		"title" : "유즈리스어덜트",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/E5EjwRG_QMVz",
		"status" : 1
	},
	{
		"idx" : 2984,
		"title" : "호똑이랑붕오랑",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/sPztGcekqzum",
		"status" : 1
	},
	{
		"idx" : 2985,
		"title" : "수저가",
		"score" : "3.9",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/GtxOzooBmnYp",
		"status" : 1
	},
	{
		"idx" : 2986,
		"title" : "블랑제메종북악",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/nkr-mTYIf02T",
		"status" : 1
	},
	{
		"idx" : 2987,
		"title" : "해로커피",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/hph8-uxwRUsE",
		"status" : 1
	},
	{
		"idx" : 2988,
		"title" : "메종드루즈",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/okCR8qH7Kn",
		"status" : 1
	},
	{
		"idx" : 2989,
		"title" : "송림원",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Wx8iSNuSEc",
		"status" : 1
	},
	{
		"idx" : 2990,
		"title" : "언니네반점",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/7CdJixcGvfT8",
		"status" : 1
	},
	{
		"idx" : 2991,
		"title" : "밀월",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/A-mUyODyhL-o",
		"status" : 1
	},
	{
		"idx" : 2992,
		"title" : "애정훠궈",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/xRh5cKO9iICe",
		"status" : 1
	},
	{
		"idx" : 2993,
		"title" : "한잔의추억",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/kwZTOjORsK",
		"status" : 1
	},
	{
		"idx" : 2994,
		"title" : "커피매터스",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/DkV1mBMwzv6Z",
		"status" : 1
	},
	{
		"idx" : 2995,
		"title" : "석관시장떡볶이",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/jwKdKwbjAl",
		"status" : 1
	},
	{
		"idx" : 2996,
		"title" : "윤휘식당",
		"score" : "3.6",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/cyoorMcUj0GC",
		"status" : 1
	},
	{
		"idx" : 2997,
		"title" : "수연산방",
		"score" : "3.6",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/x9hDSnqh-A",
		"status" : 1
	},
	{
		"idx" : 2998,
		"title" : "하단",
		"score" : "3.6",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/uZ1vyVgbOP",
		"status" : 1
	},
	{
		"idx" : 2999,
		"title" : "제순식당",
		"score" : "3.6",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/mpWAR5uKBR",
		"status" : 1
	},
	{
		"idx" : 3000,
		"title" : "옛날중국집",
		"score" : "3.6",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/VwLJ19SXdJ",
		"status" : 1
	},
	{
		"idx" : 3001,
		"title" : "성북동 이안",
		"score" : "3.6",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/aRgvAOhmGG6V",
		"status" : 1
	},
	{
		"idx" : 3002,
		"title" : "민님",
		"score" : "3.6",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/1NuFipg52EHn",
		"status" : 1
	},
	{
		"idx" : 3003,
		"title" : "매스플레이트",
		"score" : "3.6",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/RRBe9aoelJ",
		"status" : 1
	},
	{
		"idx" : 3004,
		"title" : "커피수공업",
		"score" : "3.6",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/qU5izQqaWcQO",
		"status" : 1
	},
	{
		"idx" : 3005,
		"title" : "카페브레송",
		"score" : "3.6",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/c_70oGYRAP",
		"status" : 1
	},
	{
		"idx" : 3006,
		"title" : "나폴레옹과자점",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/8GwGGYVLsP",
		"status" : 1
	},
	{
		"idx" : 3007,
		"title" : "금왕돈까스",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/4hILlPd0cD",
		"status" : 1
	},
	{
		"idx" : 3008,
		"title" : "오박사네왕돈가스",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Eg8L9NfM8X",
		"status" : 1
	},
	{
		"idx" : 3009,
		"title" : "성북동돼지갈비집",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/zJqtfDlg_b",
		"status" : 1
	},
	{
		"idx" : 3010,
		"title" : "유자유김치떡볶이",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/rCG40x4ZZI",
		"status" : 1
	},
	{
		"idx" : 3011,
		"title" : "살살솔트앤샐러드",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/6-Bay0a9hWNN",
		"status" : 1
	},
	{
		"idx" : 3012,
		"title" : "김태완의 초밥좋은날",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Ps-s-grAh-",
		"status" : 1
	},
	{
		"idx" : 3013,
		"title" : "가부",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/xwYmInBU8ivJ",
		"status" : 1
	},
	{
		"idx" : 3014,
		"title" : "놈 (휴업중)",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/ZATY3t49ln",
		"status" : 1
	},
	{
		"idx" : 3015,
		"title" : "어스핸드위치",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/DcYX1xxehZ1w",
		"status" : 1
	},
	{
		"idx" : 3016,
		"title" : "몰리다.",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/VnmIUQCDzTXK",
		"status" : 1
	},
	{
		"idx" : 3017,
		"title" : "쿠이도라쿠라멘",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/cpuxdWnDt8",
		"status" : 1
	},
	{
		"idx" : 3018,
		"title" : "라이라이라이",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/CebSzR0hOHJv",
		"status" : 1
	},
	{
		"idx" : 3019,
		"title" : "창신동매운족발",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/w3iPQA0LUq",
		"status" : 1
	},
	{
		"idx" : 3020,
		"title" : "더허브",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/dzFaNEBKUE",
		"status" : 1
	},
	{
		"idx" : 3021,
		"title" : "서울쌈냉면",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/u6K-1GzAyD",
		"status" : 1
	},
	{
		"idx" : 3022,
		"title" : "대한맥주집",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/-tXkBbcRtnkw",
		"status" : 1
	},
	{
		"idx" : 3023,
		"title" : "더베리와플",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/uiPGqHOVTA",
		"status" : 1
	},
	{
		"idx" : 3024,
		"title" : "치즈를사랑한찜닭",
		"score" : "3.5",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/BmXx5rBRmA-X",
		"status" : 1
	},
	{
		"idx" : 3025,
		"title" : "문화식당",
		"score" : "3.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/ZKlngn2dil",
		"status" : 1
	},
	{
		"idx" : 3026,
		"title" : "무르무르드구스토",
		"score" : "3.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/FiYJaiPGbn",
		"status" : 1
	},
	{
		"idx" : 3027,
		"title" : "베나레스",
		"score" : "3.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/88ULoBWcNE",
		"status" : 1
	},
	{
		"idx" : 3028,
		"title" : "쌍다리돼지불백",
		"score" : "3.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/kHgY8R-XMc",
		"status" : 1
	},
	{
		"idx" : 3029,
		"title" : "로맨틱식탁",
		"score" : "3.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/XqP-G2SmqkLO",
		"status" : 1
	},
	{
		"idx" : 3030,
		"title" : "도쿄커틀릿",
		"score" : "3.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/VYOltvWu066K",
		"status" : 1
	},
	{
		"idx" : 3031,
		"title" : "모이리타",
		"score" : "3.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Rm5HFxVxPt",
		"status" : 1
	},
	{
		"idx" : 3032,
		"title" : "마늘과올리브",
		"score" : "3.4",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/6x5tiyqdWQ",
		"status" : 1
	},
	{
		"idx" : 3033,
		"title" : "벤베누토",
		"score" : "3.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/M8Swy2pgSwjx",
		"status" : 1
	},
	{
		"idx" : 3034,
		"title" : "소테",
		"score" : "3.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Y90k-AnebL",
		"status" : 1
	},
	{
		"idx" : 3035,
		"title" : "등촌샤브칼국수",
		"score" : "3.3",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/-c8q-BgfQC",
		"status" : 1
	},
	{
		"idx" : 3036,
		"title" : "성북동 빵공장",
		"score" : "3.2",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/wDS7Lwp-AOTm",
		"status" : 1
	},
	{
		"idx" : 3037,
		"title" : "성북동디너쑈",
		"score" : "3.2",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Z8qff1O7AJ",
		"status" : 1
	},
	{
		"idx" : 3038,
		"title" : "동경산책",
		"score" : "3.2",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/NiwNsFWjGsM3",
		"status" : 1
	},
	{
		"idx" : 3039,
		"title" : "일일커피",
		"score" : "3.2",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/lx4x-7zN79ip",
		"status" : 1
	},
	{
		"idx" : 3040,
		"title" : "온달왕돈까스",
		"score" : "3.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/UmHTQryVdE",
		"status" : 1
	},
	{
		"idx" : 3041,
		"title" : "미아리우동집",
		"score" : "3.1",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/KhdpdELxMB",
		"status" : 1
	},
	{
		"idx" : 3042,
		"title" : "백소정",
		"score" : "3.0",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/nDFHyhaj2GMH",
		"status" : 1
	},
	{
		"idx" : 3043,
		"title" : "사랑마라탕",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/FGpfqeb3XN7-",
		"status" : 1
	},
	{
		"idx" : 3044,
		"title" : "삼성통닭",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/nI2v-CP5Qk",
		"status" : 1
	},
	{
		"idx" : 3045,
		"title" : "더홈서울",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/0-Og9t-csWef",
		"status" : 1
	},
	{
		"idx" : 3046,
		"title" : "문화식당",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/9ICa9tpriSj_",
		"status" : 1
	},
	{
		"idx" : 3047,
		"title" : "아뜰리에에마미",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/LBsTBjCV0R",
		"status" : 1
	},
	{
		"idx" : 3048,
		"title" : "폴드커피",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/45hwivcwmZkn",
		"status" : 1
	},
	{
		"idx" : 3049,
		"title" : "씁에스프레소바",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/2yYwDx-TvfTT",
		"status" : 1
	},
	{
		"idx" : 3050,
		"title" : "바테일러",
		"score" : "3.8",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/D3NX0UERjk9z",
		"status" : 1
	},
	{
		"idx" : 3051,
		"title" : "알렉스더커피",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/MQif8RQe96n0",
		"status" : 1
	},
	{
		"idx" : 3052,
		"title" : "프로마치",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/i9e57EcnA8",
		"status" : 1
	},
	{
		"idx" : 3053,
		"title" : "로스디아스",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/8nGkxfjCBK25",
		"status" : 1
	},
	{
		"idx" : 3054,
		"title" : "쓰리로보스",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Lqj0WP8Xkm",
		"status" : 1
	},
	{
		"idx" : 3055,
		"title" : "꽌부이",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/QUQmx0BGgaCC",
		"status" : 1
	},
	{
		"idx" : 3056,
		"title" : "포도집",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/4BuBIHVHJ6dX",
		"status" : 1
	},
	{
		"idx" : 3057,
		"title" : "태조감자국",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Mt_LGWSisQZH",
		"status" : 1
	},
	{
		"idx" : 3058,
		"title" : "커피명가",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/1pBss3WZmJ",
		"status" : 1
	},
	{
		"idx" : 3059,
		"title" : "오보록",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/YB35-4oHvp",
		"status" : 1
	},
	{
		"idx" : 3060,
		"title" : "와플앨리",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/Ol1M8CPQ6dLz",
		"status" : 1
	},
	{
		"idx" : 3061,
		"title" : "58도씨",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/6Nujr9Ou1VC3",
		"status" : 1
	},
	{
		"idx" : 3062,
		"title" : "창신동매운족발",
		"score" : "3.7",
		"region" : "성북구",
		"url" : "https://www.mangoplate.com/restaurants/tgrAJdLLNL",
		"status" : 1
	},
	{
		"idx" : 3063,
		"title" : "우리콩순두부",
		"score" : "4.4",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/Yb_icnyvZW",
		"status" : 1
	},
	{
		"idx" : 3064,
		"title" : "버거파크",
		"score" : "4.3",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/AlTrihaY1Mw7",
		"status" : 1
	},
	{
		"idx" : 3065,
		"title" : "엘림들깨수제비칼국수",
		"score" : "4.2",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/eyS1lrJkfp",
		"status" : 1
	},
	{
		"idx" : 3066,
		"title" : "춘천막국수",
		"score" : "4.2",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/yT6tRfkdamSG",
		"status" : 1
	},
	{
		"idx" : 3067,
		"title" : "벼랑순대국",
		"score" : "4.2",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/A4d4SrglLpJV",
		"status" : 1
	},
	{
		"idx" : 3068,
		"title" : "시래기화덕생선구이",
		"score" : "4.2",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/a7qpkbMwxAar",
		"status" : 1
	},
	{
		"idx" : 3069,
		"title" : "대보명가",
		"score" : "4.1",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/AiPzUgBBHN",
		"status" : 1
	},
	{
		"idx" : 3070,
		"title" : "다정도병인양",
		"score" : "4.1",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/0Dc83nt2DQsa",
		"status" : 1
	},
	{
		"idx" : 3071,
		"title" : "동네함박",
		"score" : "4.0",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/eJJqOCiiLoky",
		"status" : 1
	},
	{
		"idx" : 3072,
		"title" : "헤비앤라이트",
		"score" : "4.0",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/yhIMWujxwxtE",
		"status" : 1
	},
	{
		"idx" : 3073,
		"title" : "제이제곱",
		"score" : "4.0",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/epilCw4ynlS4",
		"status" : 1
	},
	{
		"idx" : 3074,
		"title" : "장수마늘보쌈",
		"score" : "4.0",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/7ZITxOSv9_",
		"status" : 1
	},
	{
		"idx" : 3075,
		"title" : "우디플레이트",
		"score" : "4.0",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/woz4DuWc6EWX",
		"status" : 1
	},
	{
		"idx" : 3076,
		"title" : "녹베이크샵",
		"score" : "4.0",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/Ysex0Lss6qOu",
		"status" : 1
	},
	{
		"idx" : 3077,
		"title" : "삼덕식당",
		"score" : "4.0",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/hKwPoPYVNj0D",
		"status" : 1
	},
	{
		"idx" : 3078,
		"title" : "미즐카페엠",
		"score" : "3.9",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/UqLJNWK-tFgT",
		"status" : 1
	},
	{
		"idx" : 3079,
		"title" : "하이그라운드제빵소",
		"score" : "3.9",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/hAozVMaRTyJl",
		"status" : 1
	},
	{
		"idx" : 3080,
		"title" : "히피스베이글",
		"score" : "3.9",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/Zy0b5FFvV_",
		"status" : 1
	},
	{
		"idx" : 3081,
		"title" : "천회초밥",
		"score" : "3.9",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/Z7W9ty5_ESgD",
		"status" : 1
	},
	{
		"idx" : 3082,
		"title" : "리트리트커피로스터즈",
		"score" : "3.9",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/gzQ0dIlZVZbl",
		"status" : 1
	},
	{
		"idx" : 3083,
		"title" : "다래함박스텍",
		"score" : "3.9",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/TG-Glr4P2r",
		"status" : 1
	},
	{
		"idx" : 3084,
		"title" : "김밥은",
		"score" : "3.9",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/OEHOdq0Ocozx",
		"status" : 1
	},
	{
		"idx" : 3085,
		"title" : "어셈블",
		"score" : "3.9",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/eB0Og1sqNp4O",
		"status" : 1
	},
	{
		"idx" : 3086,
		"title" : "몽브루",
		"score" : "3.9",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/Bw98ZwYwyLKY",
		"status" : 1
	},
	{
		"idx" : 3087,
		"title" : "어니언",
		"score" : "3.8",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/fdswnEC4ALoR",
		"status" : 1
	},
	{
		"idx" : 3088,
		"title" : "쿠시",
		"score" : "3.8",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/wImQ8ewGvv",
		"status" : 1
	},
	{
		"idx" : 3089,
		"title" : "원조할매곱창",
		"score" : "3.8",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/x3ZIBunCq_",
		"status" : 1
	},
	{
		"idx" : 3090,
		"title" : "카페멘디",
		"score" : "3.8",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/n8CTJqJAeMVr",
		"status" : 1
	},
	{
		"idx" : 3091,
		"title" : "무너미",
		"score" : "3.7",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/SlB-bS9zMRGx",
		"status" : 1
	},
	{
		"idx" : 3092,
		"title" : "여러분평양냉면",
		"score" : "3.7",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/YVrfus_L5rcK",
		"status" : 1
	},
	{
		"idx" : 3093,
		"title" : "양다리걸쳤네",
		"score" : "3.7",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/vJBsM6Htt3",
		"status" : 1
	},
	{
		"idx" : 3094,
		"title" : "아카데미하우스",
		"score" : "3.7",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/Ji5jVxQzEdHK",
		"status" : 1
	},
	{
		"idx" : 3095,
		"title" : "수유리조트",
		"score" : "3.7",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/WRdAd0fBcbGv",
		"status" : 1
	},
	{
		"idx" : 3096,
		"title" : "칠복상회",
		"score" : "3.6",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/M--rowLbrn2l",
		"status" : 1
	},
	{
		"idx" : 3097,
		"title" : "카페 산아래",
		"score" : "3.6",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/i3-JgN4E5QvG",
		"status" : 1
	},
	{
		"idx" : 3098,
		"title" : "옛곰탕집",
		"score" : "3.6",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/SvhgGxnzUuEQ",
		"status" : 1
	},
	{
		"idx" : 3099,
		"title" : "귀품찬",
		"score" : "3.6",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/Grl99K9qIes-",
		"status" : 1
	},
	{
		"idx" : 3100,
		"title" : "황주집",
		"score" : "3.4",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/42Iv0GNg2C",
		"status" : 1
	},
	{
		"idx" : 3101,
		"title" : "제일분식",
		"score" : "3.4",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/-BuNo6i9Ox",
		"status" : 1
	},
	{
		"idx" : 3102,
		"title" : "릴렉스",
		"score" : "3.4",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/zeU0w8VdruMz",
		"status" : 1
	},
	{
		"idx" : 3103,
		"title" : "상미규카츠",
		"score" : "3.3",
		"region" : "강북구",
		"url" : "https://www.mangoplate.com/restaurants/ixOLRn3I5Or-",
		"status" : 1
	},
	{
		"idx" : 3104,
		"title" : "코노하카레",
		"score" : "4.2",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/Jcd2gef1NuJp",
		"status" : 1
	},
	{
		"idx" : 3105,
		"title" : "마쯔무라돈까스",
		"score" : "4.2",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/NiH8HVTBC8",
		"status" : 1
	},
	{
		"idx" : 3106,
		"title" : "쌍문동판다쓰",
		"score" : "4.1",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/lUGCdfxtN2HS",
		"status" : 1
	},
	{
		"idx" : 3107,
		"title" : "원성반점",
		"score" : "4.1",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/MreZmMUSq8Gx",
		"status" : 1
	},
	{
		"idx" : 3108,
		"title" : "홍방원",
		"score" : "4.1",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/GDEdLXVumE",
		"status" : 1
	},
	{
		"idx" : 3109,
		"title" : "스마일닭강정",
		"score" : "4.1",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/NxHOALt4x3vl",
		"status" : 1
	},
	{
		"idx" : 3110,
		"title" : "수정궁",
		"score" : "4.0",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/Y74HDKIvNB",
		"status" : 1
	},
	{
		"idx" : 3111,
		"title" : "쌍문동커피",
		"score" : "4.0",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/ErtAFSOYyorW",
		"status" : 1
	},
	{
		"idx" : 3112,
		"title" : "버거브라더",
		"score" : "4.0",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/t6Fua0c9dluG",
		"status" : 1
	},
	{
		"idx" : 3113,
		"title" : "면장우동",
		"score" : "4.0",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/mDOScx3GnsXD",
		"status" : 1
	},
	{
		"idx" : 3114,
		"title" : "패멩베이커리",
		"score" : "4.0",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/kt26QH1SR-pb",
		"status" : 1
	},
	{
		"idx" : 3115,
		"title" : "쉐프마인드",
		"score" : "3.9",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/vVp9EYFBGRIB",
		"status" : 1
	},
	{
		"idx" : 3116,
		"title" : "김화자카페",
		"score" : "3.9",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/mrRpdheb5sCi",
		"status" : 1
	},
	{
		"idx" : 3117,
		"title" : "히피스베이글",
		"score" : "3.9",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/Zy0b5FFvV_",
		"status" : 1
	},
	{
		"idx" : 3118,
		"title" : "카페오븐",
		"score" : "3.9",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/XY3_mP1vjwRT",
		"status" : 1
	},
	{
		"idx" : 3119,
		"title" : "겨리",
		"score" : "3.9",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/JU9Y6M3-vYDb",
		"status" : 1
	},
	{
		"idx" : 3120,
		"title" : "도봉관",
		"score" : "3.9",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/U7ZIdNNjXFUh",
		"status" : 1
	},
	{
		"idx" : 3121,
		"title" : "참만두",
		"score" : "3.9",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/_bGwKZkNj85d",
		"status" : 1
	},
	{
		"idx" : 3122,
		"title" : "카페작약",
		"score" : "3.9",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/WCv7Qz1kr_ep",
		"status" : 1
	},
	{
		"idx" : 3123,
		"title" : "포유",
		"score" : "3.9",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/CpjUEUpf9VdH",
		"status" : 1
	},
	{
		"idx" : 3124,
		"title" : "디에그",
		"score" : "3.9",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/i77JFCEKcP4_",
		"status" : 1
	},
	{
		"idx" : 3125,
		"title" : "트라토리아진",
		"score" : "3.8",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/S-pdHBMdvGJG",
		"status" : 1
	},
	{
		"idx" : 3126,
		"title" : "피자리아150길",
		"score" : "3.8",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/N4yCAUxxbGNF",
		"status" : 1
	},
	{
		"idx" : 3127,
		"title" : "후타츠",
		"score" : "3.8",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/wxytAvCVKlbL",
		"status" : 1
	},
	{
		"idx" : 3128,
		"title" : "메이다이닝",
		"score" : "3.7",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/mzvKwo-zFX",
		"status" : 1
	},
	{
		"idx" : 3129,
		"title" : "창동짬뽕",
		"score" : "3.7",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/jOttJQnfgkLy",
		"status" : 1
	},
	{
		"idx" : 3130,
		"title" : "하누소",
		"score" : "3.7",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/JJH9FKOwsZ",
		"status" : 1
	},
	{
		"idx" : 3131,
		"title" : "동적불고기",
		"score" : "3.7",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/5zCrjQog99",
		"status" : 1
	},
	{
		"idx" : 3132,
		"title" : "햇살힐링식당",
		"score" : "3.6",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/FWR0dImCRaOA",
		"status" : 1
	},
	{
		"idx" : 3133,
		"title" : "무수옥",
		"score" : "3.6",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/BMLk3o4Sv5",
		"status" : 1
	},
	{
		"idx" : 3134,
		"title" : "사이코우스시",
		"score" : "3.6",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/-gNCobpq9T",
		"status" : 1
	},
	{
		"idx" : 3135,
		"title" : "무궁화로스터즈",
		"score" : "3.5",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/0-Cb2YWUqAGm",
		"status" : 1
	},
	{
		"idx" : 3136,
		"title" : "미미",
		"score" : "3.4",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/q6o-N9L3FX-R",
		"status" : 1
	},
	{
		"idx" : 3137,
		"title" : "글림",
		"score" : "3.3",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/CgY65yL82llU",
		"status" : 1
	},
	{
		"idx" : 3138,
		"title" : "카페고르",
		"score" : "3.1",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/_u9xEYiu7_bL",
		"status" : 1
	},
	{
		"idx" : 3139,
		"title" : "스시혼",
		"score" : "3.0",
		"region" : "도봉구",
		"url" : "https://www.mangoplate.com/restaurants/NZxK5eTxKi",
		"status" : 1
	},
	{
		"idx" : 3140,
		"title" : "제일콩집",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/tTtsd-g-1T",
		"status" : 1
	},
	{
		"idx" : 3141,
		"title" : "무명칼국수",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/EoljWc5iSb",
		"status" : 1
	},
	{
		"idx" : 3142,
		"title" : "브레드스팟",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/MGqK-XwNXxYB",
		"status" : 1
	},
	{
		"idx" : 3143,
		"title" : "광성반점",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/dENIh27cVXEp",
		"status" : 1
	},
	{
		"idx" : 3144,
		"title" : "더맛나곱창",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/LY_hL0FgkjPc",
		"status" : 1
	},
	{
		"idx" : 3145,
		"title" : "오누이",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/_i0wfVhzthzc",
		"status" : 1
	},
	{
		"idx" : 3146,
		"title" : "낙원스낵",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/43e5AhQbZ-Ha",
		"status" : 1
	},
	{
		"idx" : 3147,
		"title" : "원조닭갈비",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/KqwJ3ZugXBTZ",
		"status" : 1
	},
	{
		"idx" : 3148,
		"title" : "달콤한순간",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/nxNezZwi0VtS",
		"status" : 1
	},
	{
		"idx" : 3149,
		"title" : "브로이하우스바네하임",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/K7bmZpsjN8",
		"status" : 1
	},
	{
		"idx" : 3150,
		"title" : "구법원",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/euMIlY61D6",
		"status" : 1
	},
	{
		"idx" : 3151,
		"title" : "또와순두부수제비",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/vUFbu47ogapp",
		"status" : 1
	},
	{
		"idx" : 3152,
		"title" : "핏짜굽는언니",
		"score" : "3.8",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/7rJ-qwD2Ws",
		"status" : 1
	},
	{
		"idx" : 3153,
		"title" : "던모스",
		"score" : "3.8",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/TtRsBn-HGxzk",
		"status" : 1
	},
	{
		"idx" : 3154,
		"title" : "졸리앤몰트",
		"score" : "3.8",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/0IZ7W8QPFvNE",
		"status" : 1
	},
	{
		"idx" : 3155,
		"title" : "닭한마리",
		"score" : "3.2",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/TlTlVfmExD",
		"status" : 1
	},
	{
		"idx" : 3156,
		"title" : "홍대개미",
		"score" : "2.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/Nrgq6ldugi0-",
		"status" : 1
	},
	{
		"idx" : 3157,
		"title" : "돈까스먹는용만이",
		"score" : "3.8",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/IQVQBWzZE6",
		"status" : 1
	},
	{
		"idx" : 3158,
		"title" : "표준커피",
		"score" : "3.8",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/BswUivSqx6yd",
		"status" : 1
	},
	{
		"idx" : 3159,
		"title" : "이너모스트",
		"score" : "3.8",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/XzWWQZb4tHUd",
		"status" : 1
	},
	{
		"idx" : 3160,
		"title" : "호접몽",
		"score" : "3.8",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/jjaHDe6QJX",
		"status" : 1
	},
	{
		"idx" : 3161,
		"title" : "쉐이크쉑",
		"score" : "3.8",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/CQuLNWDMmqqJ",
		"status" : 1
	},
	{
		"idx" : 3162,
		"title" : "강강술래",
		"score" : "3.8",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/qiHT2EZUOV",
		"status" : 1
	},
	{
		"idx" : 3163,
		"title" : "스윗레시피",
		"score" : "3.8",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/IjZVsKVzBT09",
		"status" : 1
	},
	{
		"idx" : 3164,
		"title" : "싹쓰리솥뚜껑김치삼겹살",
		"score" : "3.8",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/1FYc66RKj4_P",
		"status" : 1
	},
	{
		"idx" : 3165,
		"title" : "홍익짬뽕",
		"score" : "3.7",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/tIK2sXrVVb",
		"status" : 1
	},
	{
		"idx" : 3166,
		"title" : "제형면옥",
		"score" : "3.6",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/atf72a3p5mkj",
		"status" : 1
	},
	{
		"idx" : 3167,
		"title" : "네코정",
		"score" : "3.6",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/iR-vcPQHHi12",
		"status" : 1
	},
	{
		"idx" : 3168,
		"title" : "위안바오",
		"score" : "3.6",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/BFqpBCJ1mKG5",
		"status" : 1
	},
	{
		"idx" : 3169,
		"title" : "아웃백스테이크하우스",
		"score" : "3.6",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/jqXfcvAmVl",
		"status" : 1
	},
	{
		"idx" : 3170,
		"title" : "공릉우동집",
		"score" : "3.6",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/LEMABJRyjA",
		"status" : 1
	},
	{
		"idx" : 3171,
		"title" : "피노키오냉면",
		"score" : "3.6",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/4cBErUykLR",
		"status" : 1
	},
	{
		"idx" : 3172,
		"title" : "일상다반",
		"score" : "3.5",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/lOquYsAGAv",
		"status" : 1
	},
	{
		"idx" : 3173,
		"title" : "가재골수제비",
		"score" : "3.5",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/UOf_H93aTM",
		"status" : 1
	},
	{
		"idx" : 3174,
		"title" : "메트로폴리스",
		"score" : "3.5",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/Py65Fba-v-dP",
		"status" : 1
	},
	{
		"idx" : 3175,
		"title" : "라라브레드",
		"score" : "3.4",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/QfR3LVGBCZqG",
		"status" : 1
	},
	{
		"idx" : 3176,
		"title" : "무드쉐어",
		"score" : "3.4",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/8wBr1At5eRhE",
		"status" : 1
	},
	{
		"idx" : 3177,
		"title" : "시드누아",
		"score" : "3.3",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/wZINsaP28z",
		"status" : 1
	},
	{
		"idx" : 3178,
		"title" : "원조이모네연탄불곱창",
		"score" : "3.3",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/Nzq91UaJOR",
		"status" : 1
	},
	{
		"idx" : 3179,
		"title" : "상상과자점",
		"score" : "3.3",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/-XqU_B2P3G6w",
		"status" : 1
	},
	{
		"idx" : 3180,
		"title" : "서가앤쿡",
		"score" : "3.2",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/ZfH-nE6lBq",
		"status" : 1
	},
	{
		"idx" : 3181,
		"title" : "어글리스토브",
		"score" : "3.2",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/lgbEfJP4Eg",
		"status" : 1
	},
	{
		"idx" : 3182,
		"title" : "스시하쿠야",
		"score" : "4.4",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/Zd3VyYqw8bWS",
		"status" : 1
	},
	{
		"idx" : 3183,
		"title" : "경성초밥",
		"score" : "4.3",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/HrBaIZj2EXJH",
		"status" : 1
	},
	{
		"idx" : 3184,
		"title" : "설화",
		"score" : "4.3",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/lVBstChR8L36",
		"status" : 1
	},
	{
		"idx" : 3185,
		"title" : "노원목고기집",
		"score" : "4.2",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/YW-QmiaBvf",
		"status" : 1
	},
	{
		"idx" : 3186,
		"title" : "페페그라노",
		"score" : "4.1",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/kIfLK5P0xtif",
		"status" : 1
	},
	{
		"idx" : 3187,
		"title" : "쪼매매운떡볶이",
		"score" : "4.0",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/HT9QqD1uoD",
		"status" : 1
	},
	{
		"idx" : 3188,
		"title" : "이탈리안비스트로 쿠오레",
		"score" : "4.0",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/IYTMdYMJOJnb",
		"status" : 1
	},
	{
		"idx" : 3189,
		"title" : "버거투버거",
		"score" : "4.0",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/QiyF7-iaKh",
		"status" : 1
	},
	{
		"idx" : 3190,
		"title" : "털보고된이",
		"score" : "4.0",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/fI06E_racA",
		"status" : 1
	},
	{
		"idx" : 3191,
		"title" : "땅코참숯구이",
		"score" : "4.0",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/V20BelxTkxy-",
		"status" : 1
	},
	{
		"idx" : 3192,
		"title" : "생선까시",
		"score" : "4.0",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/XR_Pm1sBGd",
		"status" : 1
	},
	{
		"idx" : 3193,
		"title" : "감동식당",
		"score" : "4.0",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/kODMC1gx_Lj0",
		"status" : 1
	},
	{
		"idx" : 3194,
		"title" : "관동식당",
		"score" : "4.0",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/T6fQ7DUeVzqd",
		"status" : 1
	},
	{
		"idx" : 3195,
		"title" : "금남커퓌",
		"score" : "4.0",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/Ew5jlPQjmqc0",
		"status" : 1
	},
	{
		"idx" : 3196,
		"title" : "중원",
		"score" : "4.0",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/9hzTOQczVCiP",
		"status" : 1
	},
	{
		"idx" : 3197,
		"title" : "노원우동짜장",
		"score" : "4.0",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/ITVAWbB_02NW",
		"status" : 1
	},
	{
		"idx" : 3198,
		"title" : "우애돈카츠",
		"score" : "4.0",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/BM4sXgU6i6u5",
		"status" : 1
	},
	{
		"idx" : 3199,
		"title" : "돈부리",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/WiuSrITuLB",
		"status" : 1
	},
	{
		"idx" : 3200,
		"title" : "썸머타이",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/DazVXhWIbHMx",
		"status" : 1
	},
	{
		"idx" : 3201,
		"title" : "디저트카페바미",
		"score" : "3.9",
		"region" : "노원구",
		"url" : "https://www.mangoplate.com/restaurants/TiiP-VMe-R",
		"status" : 1
	}
]
