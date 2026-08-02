import os

base = "/Users/susiewu/WorkBuddy/福彩_品牌联名营销知识库/weixin-articles"
out_path = "/Users/susiewu/WorkBuddy/福彩_品牌联名营销知识库/_all_text.txt"

parts = []
for d in sorted(os.listdir(base)):
    dp = os.path.join(base, d)
    if not os.path.isdir(dp):
        continue
    mds = [f for f in os.listdir(dp) if f.endswith('.md')]
    if not mds:
        continue
    fp = os.path.join(dp, mds[0])
    with open(fp, 'r', encoding='utf-8') as fh:
        raw = fh.readlines()
    # 去掉图片引用行，压缩连续空行
    text_lines = [l.rstrip() for l in raw if not l.strip().startswith('![')]
    out = []
    blank = 0
    for l in text_lines:
        if l.strip() == '':
            blank += 1
            if blank <= 1:
                out.append(l)
        else:
            blank = 0
            out.append(l)
    parts.append("=" * 80)
    parts.append("【文章】" + d)
    parts.append("=" * 80)
    parts.append("\n".join(out))

with open(out_path, 'w', encoding='utf-8') as fo:
    fo.write("\n".join(parts))

print("已合并", len(parts)//3 if parts else 0, "篇文章到 _all_text.txt")
print("总字符数:", sum(len(p) for p in parts))
