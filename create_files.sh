#!/bin/bash

upper_directories=(part_1 part_2 part_3 part_4 part_5 part_6 part_7 part_8)
part_1="air_conditioning triangle telephone_numbers ambulance equation_with_root placement_of_laptops details metro if_castle_prisoner system_of_linear_equations"
part_2="list_is_grow? type_of_sequence nearest_number bigger_than_neighbours cow_dang_championship symmetric_sequence biggest_two_multiplication biggest_three_multiplication sapper maxim_triangle"
part_3="different_numbers_count crossing_multipplicity cubes words_count open_calculator alien_genom turtles angry_pigs polyglots jogging_in_manhattan"
part_4="synonim_dict word_occurrence_number most_frequent_word keyboard pyramid sales bank_accounts deciphering_Maya_writing stress_test additional_cheating_check"
part_5="stylish_clothes numbers_sum tourism Che_city air_conditions hypercheckers_count adjustment robot triangles"
part_6="binary_search adjustment_binary_search diplomas space_settlement improving_academic_performancevery very_easy_task area wires community_work_day median_union median_union_2"
part_7="watching_for_students dots_and_segments classroom_seating advertising cash_desks contemporaries childrens_party security buses NGU-project"
part_8="tree_height added_elements_depth second_maximum detour leafs_output forks_output branchs_output AVL-balance pedigree_offspring_number pedigree_level_counting"
for upper in "${upper_directories[@]}"
do
	if [ -d $upper ]
	then
		echo "Directory $upper exist"
	else
		mkdir $upper
	fi
	temp=$(eval echo \$$upper)
	cd $upper
	for lower in $temp
	do
		if [ -d $lower ]
		then
			echo "Subdirectory $lower exist"
		else
			mkdir $lower
		fi
		cd $lower
		for file in subject.txt solution.py
		do
			if [ -e $file ]
			then
				echo "File $file exist"
			else
				touch $file
			fi
		done
		cd ..
	done
	cd ..
done