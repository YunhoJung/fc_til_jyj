#버블 정렬
정렬의 한 종류로, 가장 비효율적이지만 구현하기 쉽고 이해하기가 편해 예제용으로 자주 사용된다고 한다.

1번째와 2번째, 2번째와 3번째를 비교하는 식으로 천천히 증가했다가 다시 처음으로 돌아가는 식으로 정렬이 되며, 그 모습이 거품이 올라오는 것 같다 하여 버블 정렬이다.

__구현 코드__
	
	def bubble_sort(li):
	    len_li = len(li)-1
	    for i in range(len_li):
		print("{}번째".format(i))
		for j in range(len_li-i):
		    print("    {}".format(j))
		    if li[j] > li[j+1]:
		        li[j], li[j+1] = li[j+1], li[j]
		        print("        {}와 {}를 바꿉니다.".format(li[j],li[j+1]))
		        print("        결과:", li)
    	return li

	bubble_sort([9, 4, 1, 0, 7, 6, 2, 5, 3, 8])