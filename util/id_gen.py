# Generator ID unik kendaraan (VID - Vehicle ID)

_vid_counter = [0]

def buat_vid():
    _vid_counter[0] += 1
    return f"V-{_vid_counter[0]:04d}"

def sinkron_vid(ht):
    semua = ht.semua()
    if not semua:
        return
    maks = 0
    for v in semua:
        try:
            angka = int(v.vid.split("-")[1])
            if angka > maks:
                maks = angka
        except (IndexError, ValueError):
            pass
    _vid_counter[0] = maks