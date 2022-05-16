# overalls-color-recognition-ML

Botti, joka tunnistaa Joensuun torikamerasta opiskelijahaalareita ja ilmoittaa niistä viestillä.
Authors: Eetu Karttunen & Juuso Paakkunainen

TODO: 
- Useamman värin tunnistaminen?
- Viestin lähettäminen (twitter, telegram tms.)
- Jokin kynnysarvo, ettei ilmoiteta täysin turhista havainnoista

Käytetyt kirjastot:
- pafy
- cv2
- numpy

Pafy-kirjastosta täytyy muokata backend_youtube_dl.py tiedosta rivit 53 ja 54 muotoon:

self._likes = self._ydl_info.get('like_count',0)
self._dislikes = self._ydl_info.get('dislike_count',0)

sillä YouTube ei enää esitä dislike-tietoja julkisesti.



