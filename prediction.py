from tqdm import tqdm
import tensorflow.keras as keras
import tensorflow as tf
model=keras.models.load_model("save_at_41.h5")
pet=0;
image=[]
true=0
false=0
for img in range(117):
    
    img_="test/"+str(img)+".jpg"
    try:
        image=keras.preprocessing.image.load_img(img_,
        grayscale=False,
        color_mode='rgb',
        target_size=(180,180),
        interpolation='nearest')
        array=keras.preprocessing.image.img_to_array(image)
    except FileNotFoundError as exp:
        
        img_="test/"+str(img-1)+".jpg"
        image=keras.preprocessing.image.load_img(img_,
        grayscale=False,
        color_mode='rgb',
        target_size=(180,180),
        interpolation='nearest')
        array=keras.preprocessing.image.img_to_array(image)

    array=tf.expand_dims(array,0)
    outcome=model.predict(array)
    score=outcome[0] 
    if (pet<6):
        print("Dog-first",score,(1-score))
        if(score>(1-score)):
            true=true+1
        else:
            false=false+1
    elif(pet>=6 and pet<16):
        if((1-score)>score):true=true+1
       
        else:false=false+1
    elif (pet<70 and pet>=16):
        if(score>(1-score)):true=true+1
        else:false=false+1
    elif(pet>69):
        if((1-score)>score):true=true+1
       
        else:false=false+1
    pet=pet+1  
print("True",true)
print("False",1)
print("predictions are ",true/(true+false)*100,"% Accurate")