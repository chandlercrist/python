from television import Television 


def main():
    
    tv_1 = Television()
    tv_1.power()
    print(tv_1) 

    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.volume_up()
    print(tv_1) 

    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.channel_up()
    tv_1.volume_down()
    tv_1.volume_down()
    print(tv_1) 

    tv_1.power()
    tv_1.volume_up()
    tv_1.channel_down()
    print(tv_1) 

    tv_1.power()
    tv_1.volume_up()
    tv_1.volume_up()
    tv_1.volume_up()
    tv_1.channel_down()
    tv_1.channel_down()
    print(tv_1) 

    
    tv_2 = Television()
    tv_2.power()
    tv_2.channel_up()
    tv_2.volume_up()
    print(tv_2) 

   
    tv_1.mute()
    print(tv_1) 
    tv_1.volume_down()
    print(tv_1) 
    tv_1.mute()
    print(tv_1) 
    tv_1.volume_up()
    print(tv_1) 
    tv_1.power()
    tv_1.mute()
    print(tv_1) 
if __name__ == '__main__':
    main()