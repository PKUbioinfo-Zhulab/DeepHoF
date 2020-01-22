function codon_onehot=codon2onehot(seq,L)
r_seq=seqrcomplement(seq);

seq=upper(seq);
seq=adjust_uncertain_nt(seq);

r_seq=upper(r_seq);
r_seq=adjust_uncertain_nt(r_seq);

codon_fw1=int8(zeros(floor(L/3),64));
codon_fw2=int8(zeros(floor(L/3),64));
codon_fw3=int8(zeros(floor(L/3),64));
n=1;
for i=1:3:min(L,size(seq,2))-4
    ii=i;
    index=nt2num(seq(ii))*(4^2)+nt2num(seq(ii+1))*(4^1)+nt2num(seq(ii+2))+1;
    codon_fw1(n,index)=1;
    ii=i+1;
    index=nt2num(seq(ii))*(4^2)+nt2num(seq(ii+1))*(4^1)+nt2num(seq(ii+2))+1;
    codon_fw2(n,index)=1;
    ii=i+2;
    index=nt2num(seq(ii))*(4^2)+nt2num(seq(ii+1))*(4^1)+nt2num(seq(ii+2))+1;
    codon_fw3(n,index)=1;
    n=n+1;
end

codon_bw1=int8(zeros(floor(L/3),64));
codon_bw2=int8(zeros(floor(L/3),64));
codon_bw3=int8(zeros(floor(L/3),64));
n=1;
for i=1:3:min(L,size(r_seq,2))-4
    ii=i;
    index=nt2num(r_seq(ii))*(4^2)+nt2num(r_seq(ii+1))*(4^1)+nt2num(r_seq(ii+2))+1;
    codon_bw1(n,index)=1;
    ii=i+1;
    index=nt2num(r_seq(ii))*(4^2)+nt2num(r_seq(ii+1))*(4^1)+nt2num(r_seq(ii+2))+1;
    codon_bw2(n,index)=1;
    ii=i+2;
    index=nt2num(r_seq(ii))*(4^2)+nt2num(r_seq(ii+1))*(4^1)+nt2num(r_seq(ii+2))+1;
    codon_bw3(n,index)=1;
    n=n+1;
end

codon_fw1=codon_fw1';
codon_fw2=codon_fw2';
codon_fw3=codon_fw3';
codon_bw1=codon_bw1';
codon_bw2=codon_bw2';
codon_bw3=codon_bw3';
codon_onehot=[codon_fw1,codon_fw2,codon_fw3,codon_bw1,codon_bw2,codon_bw3];