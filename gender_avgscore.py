import pandas as pd
import os

os.chdir(os.path.dirname(__file__))
df=pd.read_csv("practice20260401.csv")
avg_male=df[df["gender"]=="男"]["score"].mean()
avg_female=df[df["gender"]=="女"]["score"].mean()

if avg_male>avg_female:
    winner="男性"
elif avg_female>avg_male:
    winner="女性"
else:
    winner="引き分け"

html = f"""
<html>
<head>
<meta charset="UTF-8">
<title>男女別平均点分析ツール</title>
</head>

<body>

<h1>男女別平均点の分析結果</h1>

<p>男性の平均点：{avg_male:.2f}</p>
<p>女性の平均点：{avg_female:.2f}</p>

<h2>結果：{winner}の平均点が高い</h2>

<h3>元データ</h3>

{df.to_html(index=False)}

</body>
</html>
"""

with open("gender_avgscore.html","w",encoding="utf-8") as f:
    f.write(html)
