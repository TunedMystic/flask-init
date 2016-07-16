var secret_key = 'this-is-a-secret-key';


function make_key(length) {
    length = length || 32;

    var alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890';
    var key = '';

    for(var i = 0; i < length; i++)
        key += alphabet.charAt(Math.floor(Math.random() * alphabet.length));

    return key;
}
