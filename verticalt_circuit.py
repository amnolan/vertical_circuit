class CircuitLoop:
  def __init__(self, ra, shared_bottom,shared_top,order):
    self.voltage_top = int(ra[0])
    self.voltage_bottom = int(ra[1])
    self.top = int(ra[2])
    self.left = int(ra[3])
    self.bottom = int(ra[4])
    self.right = int(ra[5])
    self.shared_bottom = shared_bottom
    self.shared_top = shared_top

# this code can be improved
def calculate_weights(circuitLoop, row, order):
    i1=0
    i2=0
    i3=0
    i4=0
    combined_volts = 0
    # volts = self.voltage
    if order==1:
        i1 = circuitLoop.top + circuitLoop.left + circuitLoop.right + circuitLoop.bottom
        i2 = -1 * circuitLoop.bottom 
        combined_volts = int(circuitLoop.voltage_top + circuitLoop.voltage_bottom)
    if order==2:
        i1 = circuitLoop.top*-1
        i2 = circuitLoop.left + circuitLoop.right + circuitLoop.bottom + circuitLoop.top
        i3 = circuitLoop.bottom*-1
        combined_volts = int((circuitLoop.voltage_top + circuitLoop.voltage_bottom) * -1)
    if order==3:
        i2 = circuitLoop.top*-1
        i3 = circuitLoop.left + circuitLoop.right + circuitLoop.bottom + circuitLoop.top
        i4 = circuitLoop.bottom*-1
        combined_volts = int(circuitLoop.voltage_top + circuitLoop.voltage_bottom)
    if order==4:
        i3 = circuitLoop.top*-1
        i4 = circuitLoop.left + circuitLoop.right + circuitLoop.bottom + circuitLoop.top
        combined_volts = int((circuitLoop.voltage_top + circuitLoop.voltage_bottom) * -1)
    
    row.append(i1)
    row.append(i2)
    row.append(i3)
    row.append(i4)
    row.append(combined_volts)
    return row
    
def printResult(row1,row2,row3,row4):
    print("┌                  ┐\n",
    "|",row1[0]," ",row1[1]," ",row1[2]," ",row1[3],"|\n",
    "|",row2[0]," ",row2[1]," ",row2[2]," ",row2[3],"|\n",
    "|",row3[0]," ",row3[1]," ",row3[2]," ",row3[3],"|\n",
    "|",row4[0]," ",row4[1]," ",row4[2]," ",row4[3],"|\n",
    "└                  ┘\n")
    print("Press enter to see next part of results.")
    input()
    
    print("┌                  ┐\n",
        "|i1|\n",
        "|i2|\n",
        "|i3|\n",
        "|i4|\n",
        "└                  ┘\n")
    print("Press enter to see next part of results.")
    input()
    
    print("┌                  ┐\n",
        "|",row1[4],"|\n",
        "|",row2[4],"|\n",
        "|",row3[4],"|\n",
        "|",row4[4],"|\n",
        "└                  ┘\n")


print("Is is a 4x1 circuit?, 1 for yes else 0")
yes_no = input()
if yes_no=="1":
    print("Okay! Let's solve it...\n")
else:
    print("Currently other circuit shapes can not be solved with this program")
    quit()

row1 = []
row2 = []
row3 = []
row4 = []

# this code can be improved obviously there's a lot of repetition
print("Enter comma separated: voltsT,voltsB,top ohms,left ohms,bottom ohms,right ohms for I1")

input_to_split = input()
cirlp1 = CircuitLoop(input_to_split.split(","), True, False,1)

print("Enter comma separated: voltsT,voltsB,top ohms,left ohms,bottom ohms,right ohms for I2")

input_to_split = input()
cirlp2 = CircuitLoop(input_to_split.split(","), True, False,2)

print("Enter comma separated: voltsT,voltsB,top ohms,left ohms,bottom ohms,right ohms for I3")

input_to_split = input()
cirlp3 = CircuitLoop(input_to_split.split(","), True, True,3)

print("Enter comma separated: voltsT,voltsB,top ohms,left ohms,bottom ohms,right ohms for I4")

input_to_split = input()
cirlp4 = CircuitLoop(input_to_split.split(","), False, True,4)

row1 = calculate_weights(cirlp1,row1,1)
row2 = calculate_weights(cirlp2,row2,2)
row3 = calculate_weights(cirlp3,row3,3)
row4 = calculate_weights(cirlp4,row4,4)
printResult(row1,row2,row3,row4)
