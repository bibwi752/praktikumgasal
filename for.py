# for index in "kopi robusta":
#     print(index)


# ulang =20
# for i in range(ulang):
#     print(f"perulangan ke-{i}")


# santri =("abad","afham","indra")
# kegiatan =("pramuka","jujitsu","futsal")
# for x in santri:
#     for y in kegiatan:
#         print(x,y)


mapel = ["mtk","biology","fisika","kimia","algoritma","siskom,","tkj","b.indo","dirasah islamiyah","tafsir hadis"]
# for x in mapel:
#     print(x)
#     if x=="b.indo":
#         break

for x in mapel:
    if x=="siskom":
        continue
    print(x)

    