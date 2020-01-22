function combine_predictions_1(SeqFile)
load ('./tmp/group1.mat')
group1_predict_plants = dlmread('./tmp/group1_predict_plants.csv');
group1_predict_germs =  dlmread('./tmp/group1_predict_germs.csv');
group1_predict_invertebrates = dlmread('./tmp/group1_predict_invertebrates.csv');
group1_predict_vertebrates = dlmread('./tmp/group1_predict_vertebrates.csv');
group1_predict_human = dlmread('./tmp/group1_predict_human.csv');
for i = 1:1:size(group1, 2)
	disp(i);
    prop = group1(i).group_length/group1(i).full_length;
    group1(i).plant_score = group1_predict_plants(i) * prop;
    group1(i).germs_score = group1_predict_germs(i) * prop;
    group1(i).invertebrates_score = group1_predict_invertebrates(i) * prop;
    group1(i).vertebrates_score = group1_predict_vertebrates(i) * prop;
    group1(i).human_score = group1_predict_human(i) * prop;
end
save ('./tmp/group1.mat', 'group1', '-v7.3');
clear group1 group1_predict_plants group1_predict_germs group1_predict_invertebrates group1_predict_vertebrates group1_predict_human

load ('./tmp/group2.mat')
group2_predict_plants = dlmread('./tmp/group2_predict_plants.csv');
group2_predict_germs =  dlmread('./tmp/group2_predict_germs.csv');
group2_predict_invertebrates = dlmread('./tmp/group2_predict_invertebrates.csv');
group2_predict_vertebrates = dlmread('./tmp/group2_predict_vertebrates.csv');
group2_predict_human = dlmread('./tmp/group2_predict_human.csv');
for i = 1:1:size(group2, 2)
	disp(i);
    prop = group2(i).group_length/group2(i).full_length;
    group2(i).plant_score = group2_predict_plants(i) * prop;
    group2(i).germs_score = group2_predict_germs(i) * prop;
    group2(i).invertebrates_score = group2_predict_invertebrates(i) * prop;
    group2(i).vertebrates_score = group2_predict_vertebrates(i) * prop;
    group2(i).human_score = group2_predict_human(i) * prop;
end
save ('./tmp/group2.mat', 'group2', '-v7.3');
clear group2 predict_plants group2_predict_germs group2_predict_invertebrates group2_predict_vertebrates group2_predict_human

clc;
group = fastaread(SeqFile);
load ('./tmp/group1.mat');
load ('./tmp/group2.mat');
group_all = [group1, group2];
score = struct;
for i = 1:1:size(group,1)
	disp(i);
    score(i).Header = group(i).Header;
    s = strcmp({group_all.Header}, group(i).Header);
    ind = find(s == 1);
    if isempty(ind) ~=1
        score(i).plant_score = sum(cell2mat({group_all(ind).plant_score}));
        score(i).germ_score = sum(cell2mat({group_all(ind).germs_score}));
        score(i).invertebrate_score = sum(cell2mat({group_all(ind).invertebrates_score}));
        score(i).vertebrate_score = sum(cell2mat({group_all(ind).vertebrates_score}));
        score(i).human_score = sum(cell2mat({group_all(ind).human_score}));
    end
end
writetable(struct2table(score), './tmp/score.txt');    


