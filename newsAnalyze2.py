import pandas as pd

data_df = pd.read_csv("data/코로나뉴스_감성분석.csv", encoding="euc-kr")
print(data_df.info())

print(data_df["title_label"].value_counts())  # 1과 0이 각각 몇개씩 있는지 빈도수 반환

print(data_df["description_label"].value_counts())  # 1과 0이 각각 몇개씩 있는지 빈도수 반환
# 위 빈도수 결과로 제목 title과 요약 description 간 긍정과 부정 분위기가 비슷하다고 판단됨


