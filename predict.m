function predict(DIR)
codon_files = dir([DIR,'codon*.mat']);
for i = 1:1:length(codon_files)
    codon_filenames(i) = cellstr(codon_files(i).name);
end
disp(codon_filenames);
%-----100_400bp data prediction------------------
if ismember('codon1.mat', codon_filenames)
    cmd=['python ',pwd,'/predict.py ',pwd,'/model_a.h5 ',pwd,'/tmp/sequence1.mat ',pwd,'/tmp/codon1.mat'];
    unix(cmd);
end
%-----400_800bp data prediction------------------
if ismember('codon2.mat', codon_filenames)
    cmd=['python ',pwd,'/predict.py ',pwd,'/model_b.h5 ',pwd,'/tmp/sequence2.mat ',pwd,'/tmp/codon2.mat'];
    unix(cmd);
end
