import numpy as np 
from PIL import Image as im 
from tqdm import tqdm

def main(): 
    
    # bitmap 0 - 255
    array = [[255, 255], [255, 255]]

    loop_count = int(input("How many iterations? "))

    for _ in tqdm(range(loop_count)):
        zeros = [0] * int(len(array) / 2)
        array_top = [zeros + x + zeros for x in tqdm(array)]
        array_bottom = [x + x for x in array]
        array = array_top + array_bottom

    print("Dim:", len(array[0]), "x", len(array)) 
    
    # make img
    data = im.fromarray(np.array(array, dtype=np.uint8)) 

    data.save('triangle.png') 

if __name__ == "__main__": 
    main() 
