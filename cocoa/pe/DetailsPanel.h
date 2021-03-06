/* 
Copyright 2013 Hardcoded Software (http://www.hardcoded.net)

This software is licensed under the "BSD" License as described in the "LICENSE" file, 
which should be included with this package. The terms are also available at 
http://www.hardcoded.net/licenses/bsd_license
*/

#import <Cocoa/Cocoa.h>
#import "DetailsPanelBase.h"
#import "PyDupeGuru.h"

@interface DetailsPanel : DetailsPanelBase
{
    NSImageView *dupeImage;
    NSProgressIndicator *dupeProgressIndicator;
    NSImageView *refImage;
    NSProgressIndicator *refProgressIndicator;
    
    PyDupeGuru *pyApp;
    BOOL _needsRefresh;
    NSString *_dupePath;
    NSString *_refPath;
}

@property (readwrite, retain) NSImageView *dupeImage;
@property (readwrite, retain) NSProgressIndicator *dupeProgressIndicator;
@property (readwrite, retain) NSImageView *refImage;
@property (readwrite, retain) NSProgressIndicator *refProgressIndicator;

- (id)initWithApp:(PyDupeGuru *)aApp;
@end