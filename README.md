# pygame_text_scroll
demo code showing how to scroll text line by line in PyGame

A person on youtube asked me how to simulate text being typed on pygame in a sprite. I thought that was a very 
good question, but first I had to explain how you could just display text so it could scroll.

I worked on this code to show a 'minimum' implementation of a object that could do this with a fixed delay between lines.

It is minimum, since you would probably want some other basic features like support for adding more text as it becomes avalible.

Another feature would be to speed it up in the case where two or more lines are within the time period of one *tick*. 
I just call update from update now to do this, which is not very effiencent.
