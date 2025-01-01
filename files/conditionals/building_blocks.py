def buildingblocks():
    blocks_input = int(input('Number of Blocks: '))
    height = 0
    base_layer = 1
    
    while blocks_input >= base_layer:
        blocks_input -= base_layer
        height += 1
        base_layer += 1
    
    print(f'The height of the pyramid is: {height}')

buildingblocks()
