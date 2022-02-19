
plt.plot(df['학력'],df['평균(분)'],'g--', label='학력 별 여가시간')
plt.plot(df['학력'],df['평균(분)']+100,'b-.',label='학력 별 여가시간 + 100')
plt.xlabel('학력')
plt.ylabel('여가 시간')
plt.legend(loc='best')


plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['font.size']= 7
plt.show()


#here
plt.rcParams['font.family'] = 'AppleGothic'

plt.plot(df2['소득'],df2['평균(분)'])
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['font.size']= 7
plt.show()
