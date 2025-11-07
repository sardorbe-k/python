import pandas as pd
df = pd.read_csv('tackoverflow_qa.csv')
# df.head()

# 1. Find all questions that were created before 2014
df['creationdate'] = pd.to_datetime(df['creationdate'])
result = df[df['creationdate'] < '2014-01-01']
result

# 2. Find all questions with a score more than 50

score_above_50 = df[df['score'] > 50]
print("\nQuestions with score > 50:")
print(score_above_50[['id', 'score', 'title']])

# 3. Find all questions with a score between 50 and 100
score_between = df[(df['score'] >= 50) & (df['score'] <= 100)]
print("\nQuestions with score between 50 and 100:")
print(score_between[['id', 'score', 'title']])

# 4. Find all questions answered by Scott Boston
answered_by_scott = df[df['ans_name'] == 'Scott Boston']
print("\nQuestions answered by Scott Boston:")
print(answered_by_scott[['id', 'ans_name', 'title']])

# 5. Find all questions answered by the following 5 users
users = ['Scott Boston', 'unutbu', 'Mike Pennington', 'jezrael', 'Andy Hayden']
answered_by_five = df[df['ans_name'].isin(users)]
print("\nQuestions answered by the 5 users:")
print(answered_by_five[['id', 'ans_name', 'title']])

# 6. Find all questions created between March 2014 and October 2014, answered by Unutbu, and have score < 5

mask = (
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'].str.lower() == 'unutbu') &
    (df['score'] < 5)
)
filtered = df[mask]
print("\nQuestions between March–Oct 2014, answered by Unutbu, score < 5:")
print(filtered[['id', 'creationdate', 'ans_name', 'score', 'title']])

# 7. Find all questions that have score between 5 and 10 or viewcount > 10,000
cond = ((df['score'].between(5, 10)) | (df['viewcount'] > 10000))
filtered2 = df[cond]
print("\nQuestions with score between 5–10 OR viewcount > 10000:")
print(filtered2[['id', 'score', 'viewcount', 'title']])

# 8. Find all questions not answered by Scott Boston
not_scott = df[df['ans_name'] != 'Scott Boston']
print("\nQuestions NOT answered by Scott Boston:")
print(not_scott[['id', 'ans_name', 'title']])




import pandas as pd

titanic_df = pd.read_csv("titanic.csv")

# 1️ 1-sinfdagi, yoshi 20–30 oralig‘idagi ayollar
female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]

# 2️ Narxi $100 dan yuqori yo‘lovchilar
fare_over_100 = titanic_df[titanic_df['Fare'] > 100]

# 3️ Yolg‘iz va omon qolgan yo‘lovchilar
survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]

# 4️ 'C' portidan chiqqan va $50 dan ko‘p to‘lagan yo‘lovchilar
embarked_c_fare_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]

# 5️ Ham aka-uka (SibSp > 0), ham ota-ona/bola (Parch > 0) bo‘lganlar
family_both = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]

# 6️ 15 yoshdan kichik va omon qolmaganlar
age_15_didnt_survive = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]

# 7️ Kabini bor va $200 dan yuqori yo‘l haqi to‘lagan yo‘lovchilar
cabin_fare_200 = titanic_df[
    titanic_df['Cabin'].notna() &
    (titanic_df['Fare'] > 200)
]

# 8️ PassengerId toq son bo‘lgan yo‘lovchilar
odd_id_passengers = titanic_df[titanic_df['PassengerId'] % 2 != 0]

#  9 Unikal (takrorlanmagan) Ticket raqamlari bo‘lgan yo‘lovchilar
unique_tickets = titanic_df[titanic_df['Ticket'].duplicated(keep=False) == False]

# 10 Ismida "Miss" so‘zi bor, 1-sinfda o‘qigan ayollar
miss_class1 = titanic_df[
    titanic_df['Name'].str.contains('Miss') &
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1)
]

