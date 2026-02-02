starting_position = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
from turtle import Turtle
class Snake:
          def __init__(self):
               self.new_segments = []
               self.create_snake()
               self.head = self.new_segments[0]

          def create_snake(self):
               for position in starting_position:
                    self.add_segments(position)

          def add_segments(self, position):
              segments = Turtle("square")
              segments.color("white")
              segments.penup()
              segments.goto(position)
              self.new_segments.append(segments)


          def reset(self):
             for seg in self.new_segments:
                 seg.goto(1000, 1000)
             self.new_segments.clear()
             self.create_snake()
             self.head = self.new_segments[0]



          def extend(self):
              self.add_segments(self.new_segments[-1].position())


          def move(self):
             for seg_num in range(len(self.new_segments) - 1, 0, -1):
                 new_x = self.new_segments[seg_num - 1].xcor()
                 new_y = self.new_segments[seg_num - 1].ycor()
                 self.new_segments[seg_num].goto(new_x, new_y)
             self.head.forward(MOVE_DISTANCE)

          
          def up(self):
              if self.head.heading() != 270:
                    self.head.setheading(90)

          def down(self):
              if self.head.heading() != 90:
                    self.head.setheading(270)

          def left(self):
              if self.head.heading() != 0:
                    self.head.setheading(180)

          def right(self):
              if self.head.heading() != 180:
                    self.head.setheading(0)


          

