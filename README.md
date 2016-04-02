Paket yöneticisine arayüz tasarlama programları araştırıldı.
Pisi Linux paket yöneticisinin python dili ile tasarlandığı öğrenildi.

1.Hafta
-Gerekli araştırmalar örnekler incelenmektedir.
-PyQt ve GitHub kullanımı öğrenilmektedir.

2.Hafta
-Os,Sys,Subprocess modülleri incelenmiş ve kullanımları araştırılmıştır.
-Paket Kaldirma komutları araştırılmıştır.
-Belirtilen modüllerle denemeler yapılarak proje geliştirilmeye başlanmıştır.

3.Hafta
-Kaldır metodu yazılmıştır.
-ListWidget'a paketlerin ismi bastırılmıştır.
-ListWidgetta tıklanan paketin ismi anlık(realtime) olarak alınmaktadır.
-Alınan parametre paket kaldırma komutuna eklenmektedir.
-Kaldir butonu eklenmiş ve gerekli aksiyon yazılmaya başlanmıştır.
-Paket kaldırma komutu kaldır butonuna tıklandığında çalıştırılmak üzere yazılmıştır.

4.Hafta
-Yenile butonu eklenmiştir.
-Bu butonun aksiyonu tasarlanmış ve kod aşamasına geçilmiştir.
-Yenile butonu ile lisWidget temizlenir ve hemen ardından yenilenen paket listesi tekrar listWidgeta aktarılmıştır.
-Bu olay kaldırılan paketi listwidgetta gösterilmesini ve paketlerin güncel listesinin alınması için eklenmiştir.
-Paket kaldırımı sırasında istenen yes or no cevap kısmı projede soruna yol açmıştır.
-Belirtilen kısımda python projesi donmuştur ve editör çıktı ekranından veri girişi yapılmadıkça arayüz ekranında bir işlem yapılamamaktadır.
-Bu sorun yes or no kısmını terminal ekranında bastırarak aşılmıştır.
-Kullanıcı bu sorgu ekranında sadece y veya n cevaplarını vererek paket kaldırma işlemini onaylamaktadir.
-Guncelle metodu ve butonu eklenmiştir.
-Buda varolan paketlerin tümünü güncellemek için 'apt-get update' komutunu çalıştırmaya yaramaktadır.

Tasarlanan Proje Artıları:
-Kullanıcı tüm kurulu olan paketleri görmektedir.
-Kullanıcı bu kurulu paketlerden istediğini anlık olarak seçebilmektedir.
-Anlık olarak seçilen paket direk kaldırılabilmektedir.
-Paketlerin güncellemesi tek bir butonla halledilmektedir.
-Kullanıcı yenile butonu ile sistemindeki kurulu paketlerin güncel halini sürekli alabilmektedir.

Tasarlanan Proje Eksileri:
-Proje debian kurulumları için tasarlanmıştır.
-Tasarlanan proje geliştirme sistemi root olduğu için root kullanıcılar için tasarlanmıştır.
-Kurulu program listesi çok olabilir.Bu yüzden arama kısmı eksiktir.
-Güncel paket yöneticilerinde paket ekleme ve kurma yöntemi vardır.Fakat istenilen kaldırma olduğu için paket ekle/kur kısmı yoktur.

Dipnot:
-Proje istenilen şekilde kurulu paketlerin kaldırma işlemini yapmaktadır.
-İstenilene artı olarak güncelle metodu eklenmiştir.
-Proje eksiklikleri proje yöneticisi(Doç.Dr.Ecir Uğur KÜÇÜKSİLLE) tarafından gerekli görüldüğü takdirde geliştirilmeye çalışılacaktır.
