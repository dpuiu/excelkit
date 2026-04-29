"""Unit tests for reader module."""
import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from reader import read_excel


class TestReadExcel:
    """Tests for read_excel function."""

    def test_read_excel_success(self, tmp_path):
        """Test successful Excel file reading."""
        excel_file = tmp_path / "test.xlsx"
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        df.to_excel(excel_file, index=False)
        
        result = read_excel(str(excel_file))
        
        assert result is not None
        assert len(result) == 2
        assert list(result.columns) == ["A", "B"]

    def test_read_excel_file_not_found(self):
        """Test handling of non-existent file."""
        result = read_excel("nonexistent_file.xlsx")
        
        assert result is None

    @patch("reader.pd.read_excel")
    def test_read_excel_exception(self, mock_read):
        """Test handling of read errors."""
        mock_read.side_effect = Exception("Read error")
        
        result = read_excel("dummy.xlsx")
        
        assert result is None