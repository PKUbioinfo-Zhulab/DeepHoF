function create_onehot(DIR)
fasta_files = dir([DIR,'*.fasta']);
fasta_filenames = {};
for i = 1:1:length(fasta_files)
    fasta_filenames(i) = cellstr(fasta_files(i).name);
end
%-----100_400bp data------------------
if ismember('100_400bp.fasta', fasta_filenames)
group1=fastaread([DIR,'100_400bp.fasta']);
num1 = size(group1, 1);
%%------sequence one hot-------
sequence=zeros(4,400*2, num1,'int8');%.........option
for i=1:1:size(group1,1)
    sequence(:,:,i)=nt2onehot(group1(i).Sequence,400);%....3 option 
    disp(i)
end
if size(sequence,3)~=num1 || size(sequence,2)~=400*2 %........option
    disp('error')
end
save ('tmp/sequence1.mat', 'sequence', '-v7.3');
clear sequence
%%-------codon one hot------------
codon=zeros(64, 133*6, num1,'int8');%.......option
for i=1:1:size(group1,1)
    codon(:,:,i)=codon2onehot(group1(i).Sequence,400);%...3 option
    disp(i)
end
if size(codon,3)~=num1 || size(codon,2)~=133*6 %......option
    disp('error')
end
save ('tmp/codon1.mat', 'codon', '-v7.3');
clear codon
clear group1
end
    

%-------400_800bp data------------------
if ismember('400_800bp.fasta', fasta_filenames)
group2=fastaread([DIR,'400_800bp.fasta']);
num2 = size(group2,1);
%%--------------sequence one hot-------------
sequence=zeros(4,800*2,num2,'int8');%.........option
for i=1:1:size(group2,1)
    sequence(:,:,i)=nt2onehot(group2(i).Sequence,800);%....3 option 
    disp(i)
end
if size(sequence,3)~=num2 || size(sequence,2)~=800*2%........option
    disp('error')
end
save ('tmp/sequence2.mat', 'sequence', '-v7.3');
clear sequence
%%----------codon one hot--------------
codon=zeros(64,266*6, num2,'int8');%.......option
for i=1:1:size(group2,1)
    codon(:,:,i)=codon2onehot(group2(i).Sequence,800);%...3 option
    disp(i)
end
if size(codon,3)~=num2 || size(codon,2)~=266*6 %......option
    disp('error')
end
save ('tmp/codon2.mat', 'codon', '-v7.3');
clear codon
clear group2
end
% cmd='md5sum *.mat >> md5.txt';
% unix(cmd);
