# The game map

from place import Place, HarmfulPlace
from path import Path, Door, Fire, connect
from objects import *


land = Place(
'plain boring land', 
'It is boiling hot, and feels like you are being cooked', 
'You can hear nothing but silence, which is probably because you are the only one on the island',
'You see a path up to a volcano ahead of you, and a beach west from you and forest on east of you.',
set())

beach = Place(
'a beach with lots of sand and powerful waves', 
'It is very windy, but still scorching!',
'You can hear the wind whistling, and ruffling up your clothes.',
'You can smell lots of saltiness throughout the beach. Watch out!', 
{Thing('seashell','A strange shaped blue seashell',True),Bucket()})

ocean = Place(
'the ocean.',
'The water is freezing cold, which is probably because you just got in.',
'You can hear the waves crashing onto the land, and the water whooshing.',
'You can smell the salt water that splashed all over your face, as the waves push you. Dont drown!',
{Water(),Sailboat()})

cave = Place(
'a dark cave.',
'You can barely see anything, since it is pitch black',
'It is very cool inside, and your teeth start chattering.',
'You can hear some insects chirping, and a few animals moving. Beware!',
{Flashlight()})

room = Place(
'a secret room in the cave, that no one knows of.',
'There is a small spark of light.',
'It is a decent temperature, not cold enough to shiver.',
'You can hear crickets creeking',
{Thing('key','an old rusty key',True)})


volcano = Place(
'a huge erupting volcano',
'There is lots of molten lava and rocks falling as you are reading this',
'It is very hot, as there is lava close by.',
'You can hear the lava in the volcano bubbling like a stew. Beware! It can erupt any time!',
{Battery()})


caldera = Place(
'the inside of a volcano',
'It looks very firey and dangerous, but you are desperate to escape.',
'The temperature just got even more flaming, and you feel like you are burning. Dont touch the lava!',
'You can hear rocks falling every few seconds, and feel slight shaking.',
{Thing('rock', 'a special shaped rock', True), Lava()})

chamber = HarmfulPlace(
'the deepest place in the volcano',
'You are risking your life, as you can hear the magma sputtering, and can feel the heat, burning you.',
'You feel it heavily shaking, like an earthquake, and BOOM!',
'The volcano explodes and you die.',
set(), -101)

cottage = Place(
'a small old cottage in the middle of nowhere',
'You see the closed windows and the locked door, and a few plants in front of the cottage.',
'You can already feel the warmth coming from the chimney',
'You hear silence, so you guess that there is no one living here',
set())

living_room = Place(
'a comfortable warm living room.',
'You can see a fireplace, and a couple of old sofas.',  
'You hear a creeking sound, and guess its old',
'You feel warm, and safe.',
{Scissor()})  


kitchen = Place(
'a kitchen filled with flies',
'You see lots of food, some of it being rotten',
'You can hear flies buzzing and hovering over the food',
'You smell lots of food.',
{Bottle()})

bathroom = Place(
'a very smelly bathroom',
'You see puddles of water on the floor. Looks like someone made a big mess!',
'You can hear the tap running, which either means someone was recently there, or lots of water was wasted.',
'You can see drops of blood in the bathtub.',
set())

bedroom = Place(
'a very tiny bedroom',
'You can see a bed cramped up in the corner',
'You hear the window blowing open, because of the wind.',
'You see a very unorganized shelf, full with random objects',
{Sheet(),Person()})

forest = Place(
  'a dark forest with towering trees',
  'It has been told that forest fires happen any time here.',
  'You see lots of fallen wood, and trees so tall, you cant see the sky.',
  'The trees give you lots of shade, but you have a slight feeling of flames.',
{Waterfilter()})

campground = Place(
  'an empty campground',
  'You see lots of dismantled camping tents slouching on the ground',
  'The tall trees surround you like zombies on all sides and numerous logs are piled up and have been tossed in the center.',
  'It is creepily quiet and the silence haunts you.',
{Thing('remote', 'a special shaped rock', True)})


start = land

connect(land,'west',Path(),'east',beach)
connect(beach, 'west', Path(),'east', ocean)

connect(land,'east',Path(),'west',forest)
connect(forest,'east',Fire(),'west',campground)

connect(land,'north',Door('gate',False,True,'remote'),'south',volcano)
connect(volcano,'north',Path(),'south',caldera)
connect(caldera,'north',Path(),'south',chamber)

connect(forest, 'north', Door('door', False, True, 'rock'), 'south', cave)
connect(cave, 'north', Door('door',False,True,'seashell'),'south', room)

connect(beach,'north',Door('door',False,True,'key'),'south',cottage)
connect(cottage,'north',Door(),'south',living_room)
connect(living_room,'north-east',Door(),'south-west',kitchen)
connect(kitchen, 'north', Door(), 'south', living_room)
connect(bathroom,'north-east',Door('door',False,True,'key'),'south-west',bedroom)
