Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from mcpi import minecraft
>>> import time
>>> mc = minecraft.Minecraft.create()
>>> while True:
	hits = mc.events.pollBlockHits()
	for hits in hits:
		b = mc.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z)
		if b.id == 46:
			mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, 46, 1)
			mc.postToChat("Ignite it!")

			
Traceback (most recent call last):
  File "<pyshell#10>", line 4, in <module>
    b = mc.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z)
NameError: name 'hit' is not defined
>>> 
