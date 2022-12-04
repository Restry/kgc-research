import jieba
import jieba.posseg as pseg

'''功能：添加用户自定义词典'''

sent = "周大福是创新办主任,喜欢看西部片"

# words = pseg.cut(sent)
# for word, flag in words:
#     print("{0} {1}".format(word, flag))

seg_list = jieba.cut(sent, cut_all=False)
print('未添加用户词典：', '/'.join(seg_list))

#加载用户自定义词典
jieba.load_userdict("./MachineLearning/participle_dict/genreDict.txt")

seg_list = jieba.cut(sent, cut_all=False)
print('添加用户词典：', '/'.join(seg_list))

words = jieba.posseg.cut(sent)
for word, flag in words:
    print("{0} {1}".format(word, flag))