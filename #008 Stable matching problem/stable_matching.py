def main():
    n = int(input())
    while n:
        number_of_men = int(input())
        men_pref_list = []
        for _ in range(number_of_men):
            men_pref_list.append([(woman, rank) for woman, rank in enumerate(list(map(int, input().split(' '))))])
        # sort the pref list in ascending order according to rank
        men_pref_list = [sorted(pref_list, key=lambda x: x[1]) for pref_list in men_pref_list]

        number_of_women = int(input())
        women_pref_list = []
        for _ in range(number_of_women):
            women_pref_list.append([(man, rank) for man, rank in enumerate(list(map(int, input().split(' '))))])
        # sort the pref list in ascending order according to rank
        women_pref_list = [sorted(pref_list, key=lambda x: x[1]) for pref_list in women_pref_list]

        free_men = [i for i in range(number_of_men)]
        free_women = [i for i in range(number_of_women)]
        engaged = []
        while free_men:
            current_man = free_men.pop(0)
            mans_pref = men_pref_list[current_man][:]
            for i in range(len(mans_pref), 0, -1):
                preferred_woman = mans_pref[i-1]
                if preferred_woman[0] in free_women:
                    engaged.append((current_man, preferred_woman[0]))
                    free_women.remove(preferred_woman[0])
                    mans_pref.remove(preferred_woman)
                    break
                else:
                    man_paired_with_woman = find_man_paired_with_woman(engaged, preferred_woman[0])
                    womans_pref = women_pref_list[preferred_woman[0]]
                    current_man_ranked, paired_man_ranked = find_rank_of_men(current_man, man_paired_with_woman, womans_pref)
                    if paired_man_ranked < current_man_ranked:
                        free_men.append(man_paired_with_woman)
                        engaged.remove((man_paired_with_woman, preferred_woman[0]))
                        engaged.append((current_man, preferred_woman[0]))
                        mans_pref.remove(preferred_woman)
                        break
                    mans_pref.remove(preferred_woman)
        print(engaged)
        n -= 1


def find_rank_of_men(current_man, man_paired_with_woman, womans_pref):
    paired_man_ranked = -1
    current_man_ranked = -1
    for man in womans_pref:
        if man[0] == man_paired_with_woman:
            paired_man_ranked = man[1]
        if man[0] == current_man:
            current_man_ranked = man[1]
    return current_man_ranked, paired_man_ranked


def find_man_paired_with_woman(engaged, preferred_woman):
    man_paired_with_woman = -1
    for pair in engaged:
        if pair[1] == preferred_woman:
            man_paired_with_woman = pair[0]
            break
    return man_paired_with_woman


if __name__ == '__main__':
    main()
