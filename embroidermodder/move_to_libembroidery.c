/*
    Embroidermodder 2.

    ------------------------------------------------------------

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENCE for licensing terms.

    ------------------------------------------------------------

    Preparing to move C code.
*/

double sgn(double x)
{
    if (x > 0.0) {
        return 1.0;
    }
    else {
        if (x < 0.0) {
            return -1.0;
        }
    }
    return 0.0;
}

double theta(double x)
{
    if (x < 0.0) {
        return 0.0;
    }
    return 1.0;
}

EmbVector unit_vector(float angle)
{
    EmbVector u;
    u.x = cos(angle);
    u.y = sin(angle);
    return u;
}

EmbVector rotate_vector(EmbVector a, float angle)
{
    EmbVector rot;
    EmbVector u = unit_vector(angle);
    rot.x = a.x*u.x - a.y*u.y;
    rot.y = a.x*u.y + a.y*u.x;
    return rot;
}

EmbVector scale_vector(EmbVector a, float scale)

    a.x *= scale
    a.y *= scale
    return a

EmbVector scale_and_rotate(EmbVector a, float scale, float angle):
    a = scale_vector(a, scale)
    a = rotate_vector(a, angle)
    return a
