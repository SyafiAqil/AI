import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

data = pd.read_csv('nilai_siswa.csv')
data.info()
data.head()
data.describe()

print("Rata Rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median)
print("Modus:", data['Nilai'].mode()[0])

matematika = data[data['Matpel'] == 'Matematika']
print(matematika)

Inggris = data[data['Matpel'] == 'Bahasa Inggris']
print(Inggris)

Indonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print(Indonesia)

Produktif = data[data['Matpel'] == 'Produktif']
print(Produktif)

data.groupby('Matpel')['Nilai'].agg(['max','min'])

rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Matpel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sn.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('sebaran Nilai per Mata Pelajaran')
plt.show()