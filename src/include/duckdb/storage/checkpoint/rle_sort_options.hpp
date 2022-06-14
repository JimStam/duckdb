//===----------------------------------------------------------------------===//
//                         DuckDB
//
// duckdb/storage/checkpoint/rle_sort_options.hpp
//
//
//===----------------------------------------------------------------------===//

#pragma once

#include "duckdb/common/constants.hpp"

namespace duckdb {

enum class RLESortOption : uint8_t {
	// Retrieve all columns with a cardinality < 500, sorted from lowest to highest cardinality
	CARDINALITY_BELOW_FIVE_HUNDRED = 0,
	// Use the combined hashes of multiple columns to find correlated columns
	COMBINED_CARDINALITIES = 1,
};

} // namespace duckdb
