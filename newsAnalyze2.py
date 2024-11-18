import pandas as pd
from scripts.regsetup import description

data_df = pd.read_csv("data/코로나뉴스_감성분석.csv", encoding="euc-kr")
print(data_df.info())

print(data_df["title_label"].value_counts())  # 1과 0이 각각 몇개씩 있는지 빈도수 반환

print(data_df["description_label"].value_counts())  # 1과 0이 각각 몇개씩 있는지 빈도수 반환
# 위 빈도수 결과로 제목 title과 요약 description 간 긍정과 부정 분위기가 비슷하다고 판단됨

# 감성 분석 결과를 각각 부정 label=0, 긍정 label=1 결과로 분리하여 저장
NEG_data_df = pd.DataFrame(columns=["title","title_label","description","description_label"])  # 부정 감성이 담길 빈 df
POS_data_df = pd.DataFrame(columns=["title","title_label","description","description_label"])  # 긍정 감성이 담길 빈 df

for index, data in data_df.iterrows():  # 1회전) 첫번째행이 data에 저장, index=0 2회전) 두번째행이 data에 저장, index=1
    title = data["title"]  # 1회전) 첫번째 행의 title 값
    description = data["description"]  # 1회전) 첫번째 행의 description 값
    t_label = data["title_label"]  # 1회전) 첫번째 행의 title_label 값
    d_label =  data["description_label"]  # 1회전) 첫번째 행의 description_label 값

    if d_label == 0:  # 부정 감성만 추출
        NEG_data_df = pd.concat([NEG_data_df, pd.DataFrame([[title, t_label, description, d_label]],
                                             columns=["title","title_label","description","description_label"])], ignore_index=True)
    else:
        POS_data_df = pd.concat([POS_data_df, pd.DataFrame([[title, t_label, description, d_label]],
                                                           columns=["title", "title_label", "description",
                                                                    "description_label"])], ignore_index=True)

NEG_data_df.to_csv("data/코로나뉴스_NEGATIVE.csv", encoding="euc-kr")
POS_data_df.to_csv("data/코로나뉴스_POSITIVE.csv", encoding="euc-kr")
