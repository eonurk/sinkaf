<img src="sinkaf/data/sinkaf.png" width="120" />

> _"Kötü söz sahibine aittir."_
>
> -Anonim



## Nedir?

`sinkaf` uygunsuz yorumların bulunmasını sağlayan bir python kütüphanesidir.

## Farkı nedir?

Diğer algoritmalardan en büyük farkı, önceden belirlenmiş bir kelime listesinden cümlerlerdeki sözcükleri tek tek kontrol etmek yerine, makine öğrenmesi metodları kullanarak cümlenin genel anlamına bakabilmesidir. Aynı zamanda `sinkaf` baya bi hızlı! 

## Nasıl çalışıyor?

Arka planda modelimizi eğitmek için [A corpus of Turkish offensive language](https://coltekin.github.io/offensive-turkish/guidelines.html) verisetini kullanıyoruz. Bu veriseti 36,000+ twitter yorumunun hakaret içerip içermediğini gösteren, Türkçe ile makine öğrenmesi denemeleri yapmak isteyenler için fevkaledenin fevkinde bir kaynak! Kendilerine teşekkür ediyoruz. Velhasıl...

## Nasıl yüklerim?

[![PyPI version](https://badge.fury.io/py/sinkaf.svg)](https://badge.fury.io/py/sinkaf)
[![Downloads](https://static.pepy.tech/personalized-badge/sinkaf?period=total&units=international_system&left_color=grey&right_color=orange&left_text=downloads)](https://pepy.tech/project/sinkaf)

```properties
pip3 install sinkaf
```

#### Gerekli paketler için:
``` 
pip3 install -r requirements.txt
```

## Nasıl kullanırım?

```python
from sinkaf import Sinkaf
  
snf = Sinkaf()

snf.tahmin(["çok tatlı çocuk", "çok şerefsiz çocuk"])
# array([False,  True])

snf.tahminlik(["çok tatlı çocuk", "çok şerefsiz çocuk"])
# array([0.09811712, 0.86237484])
```

### Alternatif model

[BERT](https://github.com/stefan-it/turkish-bert) kullanılarak vektörize edilmiş veri üzerinde eğitilmiş modeller:
- `bert_pre`: Küfürlü cümlelerin saptanmasında düşük duyarlılık yüksek kesinlik
- `bert_rec`: Küfürlü cümlelerin saptanmasında yüksek duyarlılık az kesinlik

```python
snf = Sinkaf(model = "bert_pre")

snf.tahmin(["çok tatlı çocuk", "çok şerefsiz çocuk"])
# array([False,  True])

snf.tahminlik(["çok tatlı çocuk", "çok şerefsiz çocuk"])
# array([0.26865139 0.85412345])

```

## İyi çalışıyor mu?
Fena değil gibi ama tabi daha iyi kesinlikle olabilir. 

Detaylar için:   
- [`sinkaf()`](sinkaf.ipynb)
- [`sinkaf(model = "bert_pre")`](sinkaf_alternatif.ipynb)


---
<a href="https://www.acikhack.com/"><img width="960" alt="image" src="https://user-images.githubusercontent.com/22842930/130684726-2bec3749-c76a-46c6-a3ac-3b34b0d84ee4.png"></a>

***sinkaf**, Açık Hack 2021<sup>\*</sup>'e katılmak amacıyla [Kara](https://github.com/eonurk)[Göz](https://github.com/ogozuacik) ekibi tarafından geliştirilmiştir.*

<div><a href="https://github.com/eonurk"><img src="https://user-images.githubusercontent.com/22842930/130747072-f0718a65-5a58-4ddd-9fda-7b127e62fc26.png" width="70" height="auto" align="absmiddle" /></a>
<a href="https://github.com/ogozuacik"> <img src="https://user-images.githubusercontent.com/22842930/130747289-afbde44d-6fe8-4a72-aaf8-31be00f4abd6.png" width="70" height="auto" align="absmiddle" /></a></div>

\
*<sup>\*[ sunum linki](https://docs.google.com/presentation/d/1J-S4mvhWRyGiFDLexv_-rvtS9EFcBDnqq6tmECWR9Q0/edit?usp=sharing), [video linki](https://www.youtube.com/watch?v=TNSMcQxTe2U&t=1s)</sup>*
