import math
from torch.utils.tensorboard.writer import SummaryWriter

if __name__ == "__main__":
    writer = SummaryWriter()
    funcs = { "sin": math.sin, "cos": math.cos, "tan": math.tan }
    
    for angle in range(-360, 360):
        angle_rad = math.radians(angle)
        for name, func in funcs.items():
            val = func(angle_rad)
            writer.add_scalar(name, val, global_step=angle)
            
    writer.close()
