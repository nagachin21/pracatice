
text = "SYZMPGWOKXIATDZYRZYPZGLIWAPGDAFDMCGDWSIKKYMINNZMG\
        CEYCJSEYMEYPMEYDPINNKDCIMDGWZIPYILLYCMYAIWAMGLGKK\
        GSMEYZMYNZGRMKDWYAFXFDMCGDWGPOMGUIJYMEYDPLRWAZZIL\
        YSYSGRKAIKZGKDJYMGIATDZYIWAPGDAAYTYKGNYPZMGZMIXMR\
        WYAIWAPYTDYSMEYDPCPXNMGOPINEDCDUNKYUYWMIMDGWZFIZY\
        AGWZYCRPYPIWAGUIWAYTIKRIMYSEYMEYPMEDZCGRKANGZYIZY\
        CRPDMXPDZJ"
        
count_str = ['a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count_result_dict = {}

for lit in count_str:
    count_num = text.count(lit.upper())
    count_result_dict[lit] = count_num

sorted_dict = sorted(count_result_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict)

def pprint(list):
    print("--------------- Frequency Table ---------------")