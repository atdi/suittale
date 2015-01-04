/**
 * Created by aurel on 1/4/15.
 */

function MeasuresHandler() {
    var url = '/api/suit_size_guides';

    this.getByType = function(type) {
        var filters = [{"name": "type", "op": "==", "val": type}];
    }

    this.getByTypeAndSize = function(type, size) {
        var filters = [{"name": "type", "op": "==", "val": type},
        {"name": "size", "op": "==", "val": size}];
    }
}