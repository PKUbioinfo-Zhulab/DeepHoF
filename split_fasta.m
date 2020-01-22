function split_fasta(inFile)
oridata = fastaread(inFile);
group1_num = 1;%100-400bp
group2_num = 1;%400-800bp
group1 = struct;
group2 = struct;
for i = 1:1:size(oridata,1)
    disp(i);
    tmp_full_length = length(oridata(i).Sequence);
    tmp_head = oridata(i).Header;
    if tmp_full_length <= 400 
        group1(group1_num).Sequence = oridata(i).Sequence;
        group1(group1_num).Header = tmp_head;
        group1(group1_num).full_length = tmp_full_length;
        group1(group1_num).group_length = tmp_full_length;
        group1_num = group1_num + 1;
    elseif tmp_full_length <= 800
        group2(group2_num).Sequence = oridata(i).Sequence;
        group2(group2_num).Header = tmp_head;
        group2(group2_num).full_length = tmp_full_length;
        group2(group2_num).group_length = tmp_full_length;
        group2_num = group2_num + 1;
    else
        tmp = mod(tmp_full_length, 800);
        num = fix(tmp_full_length/800);
        for j = 1:1:num
            group2(group2_num).Sequence =  oridata(i).Sequence((j-1)*800+1:j*800);
            group2(group2_num).Header = tmp_head;
            group2(group2_num).full_length = tmp_full_length;
            group2(group2_num).group_length = 800;
            group2_num = group2_num + 1;
        end
        if tmp ~= 0
            if tmp <= 400
                group1(group1_num).Sequence = oridata(i).Sequence(num*800+1:tmp_full_length);
                group1(group1_num).Header = tmp_head;
                group1(group1_num).full_length = tmp_full_length;
                group1(group1_num).group_length = tmp;
                group1_num = group1_num + 1;
            else
                group2(group2_num).Sequence =  oridata(i).Sequence(num*800+1:tmp_full_length);
                group2(group2_num).Header = tmp_head;
                group2(group2_num).full_length = tmp_full_length;
                group2(group2_num).group_length = tmp;
                group2_num = group2_num + 1;
            end
        end
    end
end
clear oridata

if ~isempty(group1)
    group1_fasta = struct;
    for i = 1:1:size(group1 ,2)
        disp(i);
        group1_fasta(i).Header = group1(i).Header;
        group1_fasta(i).Sequence = group1(i).Sequence;
    end
    save ('tmp/group1.mat','group1','-v7.3');
    clear group1
    fastawrite('tmp/100_400bp.fasta', group1_fasta);
    clear group1_fasta
end

if ~isempty(group2)
    group2_fasta = struct;
    for i = 1:1:size(group2 ,2)
        disp(i);
        group2_fasta(i).Header = group2(i).Header;
        group2_fasta(i).Sequence = group2(i).Sequence;
    end
    save ('tmp/group2.mat', 'group2', '-v7.3');
    clear group2
    fastawrite('tmp/400_800bp.fasta', group2_fasta);
    clear group2_fasta
end
