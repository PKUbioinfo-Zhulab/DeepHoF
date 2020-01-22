function combine_predictions(SeqFile,DIR)
prediction_files = dir([DIR,'group*_predict_plants.csv']);
if length(prediction_files) == 2
    combine_predictions_1(SeqFile)
else
    combine_predictions_2(SeqFile, DIR)
end

