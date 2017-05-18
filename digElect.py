#conding:utf-8

import pandas as pd
# import matplotlib as plt
import matplotlib.pyplot as plt
import pylab
def everyIdPlot(path):
    """
    对每个 id 生成 电量随时间变化图
    :param path:
    :return:
    """
    df = pd.read_csv(path,index_col='record_date')
    list_id = df.user_id.drop_duplicates()
    for id in list_id:
        df_temp = df[df.user_id == id]
        df_temp.plot(grid = True)
        plt.title("user_id : %s" % (id))
        # plt.plot()
        # plt.show()
        plt.savefig("e:\ %s.png" % (id))

def everydayTotalPower(path):
    """
    计算每天总的用电量，保存到 e:/to.csv  文件中
    :param path:
    :return:
    """
    df = pd.read_csv(path,index_col='record_date',parse_dates=True)
    df.plot()
    ts = df['power_consumption']
    # ts.head()
    len(ts)
    # ts.groupby('record_date').size()
    ts.groupby('record_date').sum().to_csv("e:/to.csv")

    ts.groupby('record_date').sum().plot()
    plt.show()   #   可直接显示图形
    plt.savefig("e:\out.png")  # 将结果另存

    # df1=df[df.index>='2016/1/1']
    # df1.plot(color='r')
    #
    # df2=df[df.index<'2016/1/1']
    # df2.plot(color='b')
    #
    # for index in df.index:
    #     if index < '2016/1/1':
    #         plt.plot(index,df.loc[index,'sum_power'],color='r')
    #     else:
    #         plt.plot(index,df.loc[index,'sum_power'],color='b')
    #
    #
    # print df.index


if __name__ == "__main__":
    path = "C:\Users\Administrator\Desktop\my_use\Tianchi_power.csv"
    ##  可通过调用上边两个函数生成图形
    # df = pd.read_csv(path,index_col='record_date',parse_dates=True)
    # for index in df.index:
    #     if index < '2016/1/1':
    #         plt.plot(index,df.loc[index,'sum_power'],color='r')
    #     else:
    #         plt.plot(index,df.loc[index,'sum_power'],color='b')

    plt.show()


    # everydayTotalPower(path)
