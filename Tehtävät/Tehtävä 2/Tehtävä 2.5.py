leiviskälkm = float(input("Anna leiviskät: "))
naulalkm = float(input("Anna naulat: "))
luotilkm = float(input("Anna luodit: "))




luoditg = float(13.3 * luotilkm)
naulatg = float(32 * 13.3 * naulalkm)
leiviskätg = float((32 * 13.3 * 20)*leiviskälkm)


kg = float(luoditg+naulatg+leiviskätg)
print(str(kg))




