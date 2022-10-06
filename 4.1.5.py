def list_ky_tu_dao_nguoc(ds):
    kytu=list(ds)
    kytudaonguoc=kytu[::-1]
    return kytudaonguoc
ds=input('Danh sach:')
print(ds)
